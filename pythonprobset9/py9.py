# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.
class Triangle(Shape):

    def __init__(self, base, height):
        """
        base: base of the triangle
        height: height of the triangle
        """
        self.base = float(base)
        self.height = float(height)

    def area(self):
        """
        Returns area of the Triangle
        """
        return 0.5*(self.base * self.height)

    def __str__(self):
        return 'Triangle with base ' + str(self.base) \
               + ' and height ' + str(self.height)

    def __eq__(self, other):
        """
        Two Trianglee are equal if they have the same dimensions.
        other: object to check for equality
        """
        return type(other) == Triangle and self.base == other.base\
               and self.height == other.height


#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self.set = []
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        if not sh in self.set:
            self.set.append(sh)
        ## TO DO
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        return iter(self.set)

    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO
        string = ''
        for sh in self.set:
            string += sh.__str__() + '\n'
        return string
#
# Problem 3: Find the largest shapes in a ShapeSet
#


def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    largest_shape = ()
    maxarea = max([sh.area() for sh in shapes])
    for sh in shapes:
        if sh.area() == maxarea:
            largest_shape += (sh,)
    return largest_shape
#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO
    ss = ShapeSet()
    inputFile = open(filename)
    for line in inputFile:
        a = line.split(',')
        if a[0] == 'circle':
            ss.addShape(Circle(a[1]))
        if a[0] == 'square':
            ss.addShape(Square(a[1]))
        if a[0] == 'triangle':
            ss.addShape(Triangle(a[1], a[2]))
    return ss

ss = readShapesFromFile('shapes.txt')
largest = findLargest(ss)
print "The shapes with the largest area"
for large_shape in largest:
    print large_shape


