# opencv imports
import cv2
import numpy as np 

#graph related imports
import Queue  as queue
from collections import namedtuple
import math
import random

def astar(graph, source, goal):
	# obstacle = np.random.randint(1,199)
	# obstacle = 200
	numbers = range(source-11,source-9) + range(source+9,source+11)
	''' +range(source-1)+ range(source+1)'''
	obstacle = random.choice(numbers)
	# obstacle = np.random.randint(numbers)
	print "obstacle ", obstacle
	frontier = queue.PriorityQueue()
	start = source
	lister = queue.Queue()
	frontier.put(([0, source]))
	came_from = {}
	cost_so_far = {}
	count = 0
	came_from[source] = None
	cost_so_far[source]= 0
	#print "The Source is ", source
	# print source
	qwe  = 0
	cred = 0
	while not frontier.empty():
		current = frontier.get()[1]
		
		# print "Current is ",current 
			#qwe+=1
		lister.put(current)
		if current == goal:
			path = reconstruct(current,source,came_from,goal)
			# print "Shortest path calculate"
			for _ in path:
				print _
			return path, cost_so_far[current], obstacle
	   	for i in graph.get_edge(current):
		  if math.fabs(i.vertex-current) != 1 and math.fabs(i.vertex-current) != 10 :
		        cred = 1;
		  newcost = cost_so_far[current] + i.weight+cred
		  if i.vertex not in came_from or cost_so_far[i.vertex]>newcost:
		    if i.vertex == obstacle:
		    	newcost+=10
		    cost_so_far[i.vertex] = newcost
		    priority = heuristic(graph, i.vertex, goal)+newcost
		    priority = int(priority)
		    #if qwe!= 10:
		    # print "i.vertex ", i.vertex, " cost_so_far ",cost_so_far[i.vertex]," priority ",priority," heuristic ",priority-newcost
		    frontier.put(([priority,i.vertex]))
		    came_from[i.vertex] = current



def heuristic(graph, source, destination):
	 x = int(math.ceil(source/10) )
	 x = 20 -x
	 y = 10
	 if source%10 !=0:
	 	y = source%10
	 y = 10 - y	
	 d_min = min(x,y)
	 d_max = max(x,y)
	 diag = 1.414*d_min
	 st = d_max - d_min
	 if source == 2 or source ==12:
	 	# print x,y
	 	print d_min,d_max
	 return int(diag)+st

	
def reconstruct(current,source,came_from, goal ):
	path = [current]
	# print "Source is ", source
	while current != source:

		current = came_from[current]
		# print "Currently adding ",current
		path.append(current)
	return path[: : -1]

