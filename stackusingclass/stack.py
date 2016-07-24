class Stack(object):
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)

    def pop(self):
        del self.stack[-1]

    def __str__(self):
        for i in self.stack:
            str(self.stack[-i])


    def __iter__(self):
        return iter(self.stack)

    def isempty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def __eq__(self,other):
        return type(other) == stack and cmp(self.stack,other.stack)==0

    def add(self,other):
        return self.stack = self.stack + other.stack.reverse()
