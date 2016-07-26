graph = {'A': ['B', 'C','E'],
             'B': ['A','C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F','D'],
             'F': ['C']}
import queue
#import graphs
from queue import *
#from graphs import *

qu = Queue()
node = NODE()
graph = GRAPH()

def searching(graph,start,qu):
    qu.enque([start])
    visited = graph[start]

    while qu:
        vertex = qu[0]
        if vertex not in visited :
            visited.append(vertex)
            qu.extend(graph[vertex] - visited)
    return visited
