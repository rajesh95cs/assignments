
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
a1=[]
a2=[]
word=" "
score=0
inwords=list()
subin=list()
def get_frequency_dict(word):
    freq = {}
    for x in word:
        freq[x] = freq.get(x,0) + 1
    return freq
def getwordscore(word,SCRABBLE_LETTER_VALUES):
    valid=get_frequency_dict(word)
    print(valid)
    temp=0
    for i in word :
        temp=temp+valid[i]*SCRABBLE_LETTER_VALUES[i]
    return temp

#inwords.append(subin)
for j in range(0,10):
    word=raw_input(" enter the word  ")
    print("length of the word is", len(word))
    score=getwordscore(word,SCRABBLE_LETTER_VALUES)
    a1=[word]
    a2=[len(word)]
    a3=[score]
    subin=a1+a2+a3
    print(subin)
    inwords.append(subin)


#    print(score)
print(inwords)
