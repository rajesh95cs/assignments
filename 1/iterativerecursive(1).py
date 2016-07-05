import string


def countsubstringmatchrecursive(target, key, count, c):
    b = string.find(target, key)
    # b = b + c
    if b == -1:
        print(count)
        return count
    else:
        print "Position at ", b + c + 1
        count = count + 1
        return countsubstringmatchrecursive(target[b + len(key):], key,
                                            count, c + b + len(key))

target = "atgacatgcacaagtatgcat"
key = "atga"
count = 0
c = 0
countsubstringmatchrecursive(target, key, count, c)
