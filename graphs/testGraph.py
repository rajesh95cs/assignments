"""

This is a python script to test the Graph class

"""
import graphs
from graphs import *
from string import *


# filling node list of the graph
filename = 'citylist.txt'
inputFile = open(filename)
nodenumber = 0
nodelist = []  # list of nodes
for line in inputFile:
    line = line.split('\n')[0]
    nodelist.append(NODE(nodenumber, line))
    nodenumber += 1
graph = GRAPH(nodelist)
# entering the connectivity of graph
filename = 'cityconnect.txt'
inputFile = open(filename)
for line in inputFile:
    a = line.split()
    graph.addedge(int(a[0]), int(a[1]))
# printing the graph
print " The graph connectivity is "
print graph
# printing the graph with data
print " The graph connectivity using data is "
print graph.__str__('data')
neigbours = [7, 3, 6, 8]
if set(neigbours) == set(graph.getneighbours(2)):
    print 'Test one succeeded'
neigbours = [0, 5, 1, 8]
if not set(neigbours) == set(graph.getneighbours(4)):
    print 'Test two succeeded'
