
#djikstra imports
import Queue  as queue
from collections import namedtuple

#functions for shortest path search
Edge = namedtuple('Edge', ['vertex', 'weight'])

#creating the grah class for djikstra
class GraphUndirectedWeighted(object):  
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]


#function to add a bidirectional weighted edge 
    def add_edge(self, source, dest, weight):
        assert source < self.vertex_count
        assert dest < self.vertex_count
        self.adjacency_list[source].append(Edge(dest, weight))
        self.adjacency_list[dest].append(Edge(source, weight))

    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v
    def printlist(self,x):
    	c=1;
    	for _ in self.adjacency_list[x]:

			print _ 	
			c+=1
