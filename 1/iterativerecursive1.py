import string

# a comment added
def countsubstringmatchrecursive(target,key,count,):
    b=string.find(target,key,)
    if b ==-1 :
           print(count)
           return count
    else :
          print(b)
          count=count+1
          return countsubstringmatchrecursive(target,key,count)
target="atgacatgcacaagtatgcat"
key="atgc"
count=0
b=0
countsubstringmatchrecursive(target,key,count,)
