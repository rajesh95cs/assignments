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

class GRAPH(object):
    def __init__(self,nodelist):
        self.nodes=nodelist
        self.graphconnection={}

    def addedge(self,node1number,node2number):
      if node1number < len(self.nodes) and node2number < len(self.nodes):
          if node1number in self.graphconnection :
              self.graphconnection[node1number].append(node2number)
          else:
              self.graphconnection[node1number]=[node2number]
      else :
           raise AttributeException("Nodenumber out of range")

    def addnode(self,node):
        return self.nodelist.append(node.setnumber(len(self.node)))

    #def delnode(self,nodenumber):
        #if nodenumber < len(self.nodes) :
            #del self.nodes[nodenumber]
            #del self.graphconnection[nodenumber]
            #for nodesindex in self.graphconnection:

    def getneighbours(self,nodenumber):
        if nodenumber in self.graphconnection:
            return self.graphconnection[nodenumber]
        else:
            return -1

    def getnode(self,nodenumber):
        if nodenumber < len(self.nodes):
            return self.nodes[nodenumber]
        else :
            raise AttributeException("nodenumber out of range")

    def __str__(self, flag=None):
        string = ''
        if flag is None: # normal print
            for nodeindex in self.graphconnection:
                string += "node " + str(nodeindex) + " --> " +\
                          "".join(["node " + str(i) + ", "
                                   for i in self.graphconnection[nodeindex]]) + "\n"
        if flag == 'data': # print using data
            for nodeindex in self.graphconnection:
                string += str(self.getnode(nodeindex).getdata()) + " --> " + \
                          "".join([str(self.getnode(i).getdata()) + ", "
                                   for i in self.graphconnection[nodeindex]]) + "\n"
        return string
