import string 

def countsubstringmatch(target,key): 
    b=0
    c=0
    count=0
    while b!= -1 :
       b=string.find(target,key,c)
       if b == -1 :
          break
       else:
        count=count+1
        print(b)
        c = b + 1
    print(count)
target="atgacatgcacaagtatgcat"
key="atgc"
countsubstringmatch(target,key)   
