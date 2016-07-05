import string


def countsubstringmatch(target, key):
    i=0
    b = 0
    c = 0
    alist[:]
    alist[0:len(target)]=0
    count = 0
    while b != -1:
        b = string.find(target, key, c)
        if b == -1:
            break
        else:
            count = count+1
        print "Position at ", b
        alist[i:]=b
        i=i+1
        c = b + 1
    print(count)
    atuple=tuple(alist)
    print(atuple)
    print "tuple="
target = "atgacatgcacaagtatgcat"
key = "atgc"
countsubstringmatch(target, key)
