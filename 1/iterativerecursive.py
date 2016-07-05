import string


def countsubstringmatchrecursive(target, key, count, c):
    b = string.find(target, key,c)
    c=b+1
    if b == -1 :
        print(count)
        return count
    else:
        print "Position at ", b
        count = count + 1
        return countsubstringmatchrecursive(target, key, count, c)

target = "atgacatgcacaagtatgcat"
key = "atgc"
count = 0
c = 0
countsubstringmatchrecursive(target, key, count, c)
