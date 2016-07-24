"""

This is a python script to test the Stack class

"""
import stack
from stack import *
from string import *

s1 = stack()
s2 = stack()
# filling first stack
filename = 'list1.txt'
inputFile = open(filename)
for line in inputFile:
    s1.push(line)
# filling second stack
filename = 'list2.txt'
inputFile = open(filename)
for line in inputFile:
    s2.push(line)
# printing both the stacks
# print stack one
print " Stack one has"
print s1
# print stack two
print " Stack two has"
print s2
# concatenating two stacks
s3 = s1 + s2
# printing stack three
print " Stack three has"
print s3
# new stack
s4 = Stack()
s4.push('Rest of the elements are from stack s3')
# poping all the elements in s3 and pushing it to s4
while not s3.isempty():
    s4.push(s3.pop())
# Should print the elements in s3 in reverse
# when printing s4
print " Stack four has"
print s4
# Should print the stack is empty
print " Stack three has"
print s3
# filling three stack
filename = 'list3txt'
inputFile = open(filename)
for line in inputFile:
    a = line.split(',')
    s3.push((a[0], a[1]))
print " Stack s3 contains"
print s3
# iterate over the stack s3
for element in s3:
    print type(element)
# check equality
s5 = Stack()
s6 = Stack()
# filling both stacks
filename = 'list1.txt'
inputFile = open(filename)
for line in inputFile:
    s5.push(line)
    s6.push(line)
if s5 == s6:
    print "The stacks contains the same elements"
