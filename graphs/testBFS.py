"""

This is a python script to test the Breath first search class

The script generates a graphs which is a discrete representation of a domain
with both x and y axis varying -30 to 30. BFS is performed on this graph from
a start node
"""
import graphs
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from graphs import *
from string import *
from breadthfirstsearch import *

nodelist = []
nodenumber = 0
# change the xrange and yrange for different domain size
xrange = [-30, 30]
yrange = [-30, 30]
xlen = len(range(xrange[0], xrange[1] + 1))
ylen = len(range(yrange[0], yrange[1] + 1))
fig = plt.figure()
plt.hold(True)
for i in range(xrange[0], xrange[1] + 1):
    plt.plot([i, i], [yrange[0], yrange[1]], 'y')
for i in range(yrange[0], yrange[1] + 1):
    plt.plot([xrange[0], xrange[1]], [i, i], 'y')
# filling the graph with node list containing coordinates of points
for j in range(yrange[0], yrange[1] + 1):
    for i in range(xrange[0], xrange[1] + 1):
        plt.plot(i, j, 'b.')  # ploting the coordinates
        nodelist.append(NODE(nodenumber, (i, j)))
        nodenumber += 1
graph = GRAPH(nodelist)
startcoord = (0, 0)
startnodenumber = 0
# adding the edges to the graph
for node in nodelist:
    x, y = node.getdata()
    nodenumber = node.getnumber()
    # finding start node
    if x == startcoord[0] and y == startcoord[1]:
        startnodenumber = nodenumber
    # points not in corners or edges
    if xrange[0] < x < xrange[1] and yrange[0] < y < yrange[1]:
        graph.addedge(nodenumber, nodenumber + xlen)  # top node
        graph.addedge(nodenumber, nodenumber - xlen)  # bottom node
        graph.addedge(nodenumber, nodenumber + 1)  # right node
        graph.addedge(nodenumber, nodenumber - 1)  # left node
    else:
        # top edge
        if y == yrange[1] and x != xrange[0] and x != xrange[1]:
            graph.addedge(nodenumber, nodenumber - xlen)  # bottom node
            graph.addedge(nodenumber, nodenumber + 1)  # right node
            graph.addedge(nodenumber, nodenumber - 1)  # left node
        else:
            # left corners
            if y == yrange[1] and x == xrange[0]:
                graph.addedge(nodenumber, nodenumber - xlen)  # bottom node
                graph.addedge(nodenumber, nodenumber + 1)  # right node
                # right corners
            if y == yrange[1] and x == xrange[1]:
                graph.addedge(nodenumber, nodenumber - xlen)  # bottom node
                graph.addedge(nodenumber, nodenumber - 1)  # left node
        # bottom edge
        if y == yrange[0] and x != xrange[0] and x != xrange[1]:
            graph.addedge(nodenumber, nodenumber + xlen)  # top node
            graph.addedge(nodenumber, nodenumber + 1)  # right node
            graph.addedge(nodenumber, nodenumber - 1)  # left node
        else:
            # left corners
            if y == yrange[0] and x == xrange[0]:
                graph.addedge(nodenumber, nodenumber + xlen)  # top node
                graph.addedge(nodenumber, nodenumber + 1)  # right node
            # right corners
            if y == yrange[0] and x == xrange[1]:
                graph.addedge(nodenumber, nodenumber + xlen)  # top node
                graph.addedge(nodenumber, nodenumber - 1)  # left node
        # left edge
        if x == xrange[0] and y != yrange[0] and y != yrange[1]:
            graph.addedge(nodenumber, nodenumber + xlen)  # top node
            graph.addedge(nodenumber, nodenumber - xlen)  # bottom node
            graph.addedge(nodenumber, nodenumber + 1)  # right node
        # right edge
        if x == xrange[1] and y != yrange[0] and y != yrange[1]:
            graph.addedge(nodenumber, nodenumber + xlen)  # top node
            graph.addedge(nodenumber, nodenumber - xlen)  # bottom node
            graph.addedge(nodenumber, nodenumber - 1)  # left node
# print graph
# calling bfs function
traverse = bfs(graph, startnodenumber)
# print traverse
# plotting the start node
x, y = graph.getnode(startnodenumber).getdata()
line, = plt.plot(x, y, 'rs')
x_loc = []
y_loc = []
max_frame = len(traverse)
def animate(i_loc):
    x_data, y_data = graph.getnode(traverse[i_loc]).getdata()
    x_loc.append(x_data)
    y_loc.append(y_data)
    line.set_xdata(x_loc)
    line.set_ydata(y_loc)  # update the data
    return line,


def init():
    line.set_xdata(x)
    line.set_xdata(y)
    return line,

plt.xlim(xrange[0], xrange[1])
plt.ylim(yrange[0], yrange[1])
plt.xlabel("X")
plt.ylabel("Y")
ani = animation.FuncAnimation(fig, animate, range(0, max_frame), init_func=init,
                                  interval=10, blit=True, repeat=False)
# ani.save('BFS_animation.mp4', fps=20, writer="avconv", codec="libx264")
plt.show()



