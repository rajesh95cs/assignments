import queue
from queue import *
qu =
graph = {}
class CREATE(object):
    def __init__(self):
        self.graph = {}

    def creategraph(self,node1,node2):
        for key in self.graph :
            self.graph[key] == []

        if node1 in self.graph and node2 in self.graph :
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
        else :
            self.graph[node1] = [node2]
            self.graph[node2] = [node1]
        return self.graph

def searching(graph,start):
    visited = graph[start]
    qu = [start]
    while qu:
        vertex = qu[0]
        if vertex not in visited :
            visited.append(vertex)
            qu.extend(graph[vertex] - visited)
    return visited
