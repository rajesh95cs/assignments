class Stack(object):
    def __init__(self):
        self.container = []
    def push(self,element):
        self.container.append(element)

    def pop(self):
         popedelemnt = self.container[-1]
         del self.container[-1]
         return popedelemnt

    def __str__(self):
        if self.isempty():
            return "the stack is empty"
        else:
            return str(self.container)


    def __iter__(self):
        return iter(self.container)

    def isempty(self):
        if len(self.container) == 0:
            return True
        else:
            return False
    def __eq__(self , other):
        return type(other) == Stack and cmp(self.container,other.container)==0

    def __add__(self , other):
        netStack = Stack()
        netStack.container = self.container + other.container
        return netStack
