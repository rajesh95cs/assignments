import stack
from stack import *

def dfs(graph,start):
    st = Stack()
    st.push(start)
    visited = [start]
    traversed = []
    while not st.isempty():
        vertex = st.pop()
        traversed.append(vertex)
        for neighbour in graph.getneighbours(vertex) :
            if neighbour not in visited :
                st.push(neighbour)
                visited.append(neighbour)
    return traversed
