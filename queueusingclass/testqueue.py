"""

This is a python script to test the Stack class

"""
import queue
from queue import *
from string import *

q1 = Queue()
q2 = Queue()
# filling first Queue
filename = 'list1.txt'
inputFile = open(filename)
for line in inputFile:
    q1.enque(line)
# filling second Queue
filename = 'list2.txt'
inputFile = open(filename)
for line in inputFile:
    q2.enque(line)
# printing both the Queue
# print Queue one
print " Queue one has"
print q1
# print Queue two
print " Queue two has"
print q2
# concatenating two Queues
q3 = q1 + q2
# printing Queue three
print " Queue three has"
print q3
# new Queue
q4 = Queue()
q4.enque('Rest of the elements are from Queue q3')
# dequeueing all the elements in q3 and enque it to q4
while not q3.isempty():
    q4.enque(q3.deque())
# when printing s4
print " Queue four has"
print q4
# Should print the Stack is empty
print " Queue three has"
print q3
# filling three Stack
filename = 'list3.txt'
inputFile = open(filename)
for line in inputFile:
    a = line.split(',')
    q3.enque((a[0], a[1]))
print " Queue s3 contains"
print q3
# iterate over the Queue q3
for element in q3:
    print type(element)
# check equality
q5 = Queue()
q6 = Queue()
# filling both Queue
filename = 'list1.txt'
inputFile = open(filename)
for line in inputFile:
    q5.enque(line)
    q6.enque(line)
if q5 == q6:
    print "The Queues contains the same elements"
