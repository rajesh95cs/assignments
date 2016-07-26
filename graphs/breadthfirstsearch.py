import queue
from queue import *

def bfs(graph,start):
    qu = Queue()
    qu.enque([start])
    visited = start
    traversed = []
    while not qu.isempty():
        vertex = qu.deque()
        traversed.append(vertex)
        for neighbour in graph.getneighbours(vertex) :
            if neighbour not in visited :
                qu.enque(neighbour)
                visited.append(neighbour)
    return traversed
