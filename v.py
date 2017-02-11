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

#delay imports
import time


def create_image(botx,boty,ballx,bally, take):
		width, height = 1000, 500
		white = (255, 255, 255)
		image = create_blank(width, height, rgb_color=white)		
	    
		cv2.circle(image,(botx,boty),19,(255,0,0),-1)
		cv2.circle(image,(ballx,bally),13,(0,255,0),-1)

		#displaying the grids
		i = 0
		while i<=500:
			cv2.line(image, (0, i), (1009, i), (0,0,255), 1)
			i=i+50

		i = 0
		while i<=1000:
			cv2.line(image, (i, 0), (i, 564), (0,0,255), 1)
			i=i+50

		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(image,str(take),(450,240), font, 1,(0,0,0),2)
		cv2.imwrite("white.jpg", image)

		
		

		

def main():	

	ballx = input("Enter initial x cordinate of ball  ")
	bally = input("Enter initial y cordinate of ball  ")
	botx = input("Enter initial x cordinate of bot  ")
	boty = input("Enter initial y cordinate of bot  ")

	take = 1
	create_image(botx,boty,ballx, bally, take)

	
		
	while 1:
		flag = 0
		start = time.time()
		

		image = cv2.imread("white.jpg")
		cv2.imshow('image', image)
		cv2.waitKey(10)

		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		
		lower_blue = np.array([110,50,50])
		upper_blue = np.array([130,255,255])

		mask = cv2.inRange(hsv, lower_blue, upper_blue)

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
		
		goal = 200
		shortest_path, distance, obstacle = astar(g, source, ball)
		obstaclex, obstacley = get_center(obstacle)
		for i in shortest_path:	
			if (time.time()-start < 1):

				botx, boty = get_center(i)
				create_image(botx,boty,ballx, bally,take)
				
				image = cv2.imread("white.jpg")
				cv2.circle(image,(obstaclex,obstacley),13,(0,0,255),-1)
				cv2.imshow('image', image)
				cv2.waitKey(333)
			else:
				flag = 1
				break
			
		if flag==1:
				continue
		

		shortest_path, distance, obstacle = astar(g, ball, goal)
		obstaclex, obstacley = get_center(obstacle)
		for i in shortest_path:
			if(time.time()-start < 1):
				botx, boty = get_center(i)
				ballx, bally = botx, boty
				create_image(botx, boty, ballx, bally, take)
				
				image = cv2.imread("white.jpg")
				cv2.circle(image,(obstaclex,obstacley),13,(0,0,255),-1)
				cv2.imshow('image', image)
				cv2.waitKey(333)
			else:
				flag = 1
				break

		if flag==1:
				continue


		x=np.random.randint(1,1000)
		y=np.random.randint(1,500)	
		ballx=np.random.randint(1,1000)
		bally=np.random.randint(1,500)	
		take+=1
		create_image(x,y,ballx, bally, take)
		time.sleep(2)
		# cv2.destroyAllWindows()



if __name__ == "__main__":  
    main()









