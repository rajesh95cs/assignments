import string
subdicc={}
maxwork=15
def cmpWork(subInfo1, subInfo2):

   # Returns True if work in (value, work) tuple subInfo1 is LESS than than work
   #in (value, work) tuple in subInfo2 """
    work1 = subInfo1[1]
    #print "subInfo1[1] = ",work1
    work2 = subInfo2[1]
    #print "subInfo2[1] = ",work2
    print "work1 < work2 = ",work1 < work2
    return  work1 < work2

def greedyadvisor(subdicc,maxwork,compWork):
    add = 0
    subNames = subdicc.keys()
    print len(subdicc)
    for i in range(0,len(subdicc)):
        if i+1 <= len(subdicc):
            val = subdicc[subNames[i]][0]
            #print " subdicc[subNames[i]][0] = ",val
            work = subdicc[subNames[i]][1]
            #print " subdicc[subNames[i]][1] = ",work
            val1=subdicc[subNames[i+1]][0]
            work1=subdicc[subNames[i+1]][1]
            isgreater=compWork((val,work),(val1,work1))
            if  isgreater==True :
                if add < maxwork:
                    print "max work = ",maxwork
                    x = subdicc[subNames[i+1]][1]
                    #print "subdicc[subNames[i+1]][1] = ",x
                    add = add + subdicc[subNames[i+1]][1]
                    print "add before condition satisfied",add
                    #print "index i = ",i
                    #print "added work = ",add
                    #print val
                    #print work
                    #print "val1 = ",val1
                    #print "work1 = ",work1
                    print "{",subNames[i+1],":",subdicc[subNames[i+1]],"}"
                else:
                    break

        else :
            break

def loadSubjects():
    subdicc={}

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile=open("subjects.txt",'r')
    for line in inputFile :
        a=line.split(',')
        a[1]=int(a[1])
        a[2]=int(a[2])
        subdicc[a[0]]=(a[1],a[2])
    #printSubjects(subdicc)
    greedyadvisor(subdicc,maxwork,cmpWork)

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subdicc):
    subNames=[]
    totalVal, totalWork = 0,0
    if len(subdicc) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subdicc.keys()
    subNames.sort()
    for s in subNames:
        val = subdicc[s][0]
        work = subdicc[s][1]
        print val ,"   ", work
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

loadSubjects()
"""
def cmpValue(subInfo1, subInfo2):

    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2

    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2
"""

"""
def cmpRatio(subInfo1, subInfo2):

    Returns True if value/work in (value, work) tuple subInfo1 is
    GREATER than value/work in (value, work) tuple in subInfo2

    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2
"""
