str="atgacatgcacaagtatgcat"
ch="atgc"
index=1
def find(str, ch):
    while index < len(str):
        if str[index] == ch:
           print(index)
           return index
        index = index + 1
    return -1
print(index)
