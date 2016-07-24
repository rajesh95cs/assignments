class stack(object):
    def __init__(self):
        self.container = []
    def push(self,element):
        self.container.append(element)

    def pop(self):
        del self.contain[-1]

    def __str__(self):
            return str(self.container)


    def __iter__(self):
        return iter(self.container)

    def isempty():
        if len(self.container) == 0:
            return True
        else:
            return False
    def __eq__(self , other):
        return type(other) == stack and cmp(self.container,other.stack)==0

    def __add__(self , other):
        netstack = stack()
        netstack.container = self.container + other.container
        return netstack
