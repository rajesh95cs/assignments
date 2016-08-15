
word = "everyone"
def reverse(word):
    count = 0
    for i in word :
        count = count + 1
    toberev = []
    for i in range(count):
        toberev.append(word[(count-1)-i])
        #print word[(count-1)-i]
    word = toberev
    return word
revword = reverse(word)
print revword
