class Queue(object):
    def __init__(self):
        self.container = []
    def enque(self,element):
        self.container.append(element)

    def deque(self):
         popedelemnt = self.container[0]
         del self.container[0]
         return popedelemnt

    def __str__(self):
        if self.isempty():
            return "the Queue is empty"
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
        return type(other) == Queue and cmp(self.container,other.container)==0

    def __add__(self , other):
        netQueue = Queue()
        netQueue.container = self.container + other.container
        return netQueue
