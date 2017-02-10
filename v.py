# opencv imports
import cv2
import numpy as np
from opencv_functions import get_center, get_block_no_rand, create_blank 

#queue , tuple imports 
import Queue  as queue
from collections import namedtuple

#algo imports
from dijkstra import dijkstra
from astar import astar 
import math

#graph imports
from graph_func import GraphUndirectedWeighted


#test function to print adjacency list

#main function
#the tasks to be performed in main function
# 1: get the position of centre of mass of the robot
# 2: get the node number in which it is located currently
# 3: perform djikstra shortest path search which this node as source to goal
def main():

	width, height = 1000, 500

	white = (255, 255, 255)
	image = create_blank(width, height, rgb_color=white)

	#x=np.random.randint(1,1000)
	#y=np.random.randint(1,500)
	ballx = input("Enter x cordinate of ball  ")
	bally = input("Enter y cordinate of ball  ")
	x = input("Enter x cordinate of bot  ")
	y = input("Enter y cordinate of bot  ")
    #print "Cordinated rcvd ",x,y
	cv2.circle(image,(x,y),13,(255,0,0),-1)
	cv2.circle(image,(ballx,bally),13,(0,0,0),-1)

	cv2.imwrite('white.jpg', image)
	image = cv2.imread("white.jpg")

	#displaying the grids
	i = 0
	while i<=500:
		cv2.line(image, (0, i), (1009, i), (0,0,255), 1)
		i=i+50

	i = 0
	while i<=1000:
		cv2.line(image, (i, 0), (i, 564), (0,0,255), 1)
		i=i+50

	# Convert BGR to HSV
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	# define range of blue color in HSV
	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(image,image, mask= mask)
	max=0.0
	contours,hry = cv2.findContours(mask,1,2)
	for i in contours:
		cnt=cv2.contourArea(i)
		if((cnt>max) and (cnt>20)):
			max=cnt
			bst_cnt=i
	 		# print max

	M = cv2.moments(bst_cnt)
	#print M
	if M['m00']!=0:
		cx=int(M['m10']/M['m00'])
		cy=int(M['m01']/M['m00'])
		print "Bot" ,cx,cy
	else:
		print M['m00'],"For Bot" 

	source = get_block_no_rand(cx, cy)
	print source


	g = GraphUndirectedWeighted(201)
	'''i=1
	while(i<=200):
	    if(i%50):
	        g.add_edge(i, i+1, 1)
	    i+=1
	i=1
	while(i<=200):
	    if(i+10<=200):
	        g.add_edge(i, i+10, 1)
	    if(i%5):
	        if(i+11<=200):
	            g.add_edge(i, i+11, 1)
	    i+=1
'''
#edits by shukla
	num_of_rows = 10
	num_of_columns = 20
	i=1
	while(i<=200):
	    if(i%10):#changed 50 to 10
	        g.add_edge(i, i+1, 1)
	    	if(i+num_of_rows+1<=200):
	        	g.add_edge(i, i+num_of_rows+1, 1)    
	    i+=1
	i=1

	while(i<=200):
	    if(i+num_of_rows<=200):
	        g.add_edge(i, i+num_of_rows, 1)
	    if(i+num_of_rows-1<=200 and (i%num_of_rows!=1)):
	        g.add_edge(i, i+num_of_rows-1, 1)
	    
	    
	    i+=1
	g.printlist(10)

	ball = get_block_no_rand(ballx,bally)
	#assuming goal to be cornermost point
	goal = 200
	shortest_path, distance = astar(g, source, ball)
	for i in shortest_path:
		# print i
		x, y = get_center(i)
		cv2.circle(image,(x,y),13,(0,0,255),-1)

	shortest_path, distance = astar(g, ball, goal)
	for i in shortest_path:
		# print i
		x, y = get_center(i)
		cv2.circle(image,(x,y),10,(0,255,0),-1)
	

	# assert shortest_path == [0, 1] and distance == 4

	cv2.imshow('image',image)
	# cv2.imshow('mask',mask)
	# cv2.imshow('res',res)
	cv2.waitKey(0)
	cv2.destroyAllWindows()



if __name__ == "__main__":  
    main()









