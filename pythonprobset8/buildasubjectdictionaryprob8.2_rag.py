import string


def cmpWork(subInfo1, subInfo2):

   # Returns True if work in (value, work) tuple subInfo1 is LESS than than work
   #in (value, work) tuple in subInfo2 """
    work1 = subInfo1[1]
    #print "subInfo1[1] = ",work1
    work2 = subInfo2[1]
    #print "subInfo2[1] = ",work2
    # print "work1 < work2 = ",work1 < work2
    return  work1 < work2


def greedyadvisor(subdicc, maxwork, comparator):
    add = 0
    subNames = subdicc.keys()
    bestsubnames = []
    selected = {}
    print len(subdicc)
    while add < maxwork:
        bestsubnames.append(subNames[0])
        for i in range(len(subNames) - 1):
            if comparator(subdicc[bestsubnames[-1]], subdicc[subNames[i]]) \
                    and subdicc[subNames[i]] < maxwork:
                bestsubnames[-1] = subNames[i]
        add += subdicc[bestsubnames[-1]][1]
        if add > maxwork:
            del bestsubnames[-1]
            break
        subNames.remove(bestsubnames[-1])
    for keys in bestsubnames:
        selected[keys] = subdicc[keys]
    return selected


def loadSubjects():

    # The following sample code reads lines from the specified file and prints
    # each one.
    subdicc = {}
    inputFile = open("subjects.txt", 'r')
    for line in inputFile:
        a = line.split(',')
        subdicc[a[0]] = (int(a[1]), int(a[2]))
    return subdicc
    # printSubjects(subdicc)


    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subdicc):
    subNames = []
    totalVal, totalWork = 0, 0
    if len(subdicc) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subdicc.keys()
    subNames.sort()
    for s in subNames:
        val = subdicc[s][0]
        work = subdicc[s][1]
        print val, "   ", work
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) + '\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res




def cmpValue(subInfo1, subInfo2):

    # Returns True if value in (value, work) tuple subInfo1 is GREATER than
    # value in (value, work) tuple in subInfo2

    val1 = subInfo1[0]
    val2 = subInfo2[0]
    return  val1 > val2



def cmpRatio(subInfo1, subInfo2):

    # Returns True if value/work in (value, work) tuple subInfo1 is
    # GREATER than value/work in (value, work) tuple in subInfo2

    val1 = subInfo1[0]
    val2 = subInfo2[0]
    work1 = subInfo1[1]
    work2 = subInfo2[1]
    return float(val1) / work1 > float(val2) / work2

# Program starts
subdicc = loadSubjects()
maxwork = 15
selected = greedyadvisor(subdicc, maxwork, cmpValue)
printSubjects(selected)
selected = greedyadvisor(subdicc, maxwork, cmpWork)
printSubjects(selected)
selected = greedyadvisor(subdicc, maxwork, cmpRatio)
printSubjects(selected)
