class NODE(object):
    def __init__(self,number,data):
        self.number=number
        self.data=data

    def getnumber(self):
        return self.number

    def getdata(self):
        return self.data

    def setdata(self,data):
        self.data = data

    def setnumber(self,number):
        self.number = number

    def __str__(self):
        return "the number of the node is " + str(self.number) + " and its data is " + str(self.data)

    def __eq__(self,other):
        return type(other) == NODE and ( self.number == other.number and self.data == other.data )

n1 = NODE(1,"hi")
n2 = NODE(2,"hello")
print n1
print n1.getnumber
print n2.getdata
n2.setnumber = n1.getnumber
n2.setdata(n1.getdata)
print n1==n2
