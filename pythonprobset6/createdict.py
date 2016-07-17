
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
word=" "
dicc={}
word_list=["aahh","haha","bombay","delhi","bah","cab","coder","good"]
dicword=[]
def get_frequency_dict(word):
    freq = {}
    for x in word:
        freq[x] = freq.get(x,0) + 1
    return freq
def getwordscore(word,SCRABBLE_LETTER_VALUES):
    valid=get_frequency_dict(word)
    temp=0
    for i in word :
        temp=temp+valid[i]*SCRABBLE_LETTER_VALUES[i]
    return temp
def pointdict(word_list):
    for i in range(len(word_list)):
        lenword=len(word_list[i])
        word=word_list[i]
        if lenword not in dicc.keys():
            score=getwordscore(word,SCRABBLE_LETTER_VALUES)
            dicc[lenword]={score:[word]}
        else :
            score=getwordscore(word,SCRABBLE_LETTER_VALUES)
            if score in dicc[lenword].keys():
                dicc[lenword]={score:dicword.append(word)}

pointdict(word_list)
print(dicc)
