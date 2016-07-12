import random
import string


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
nex={}
VOWELS ="aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def load_words():
    print "Loading word list from file..."
    inFile = open(words.txt, 'r', 0)
    words = []
    for line in inFile:
        words.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return words


def get_frequency_dict(word):
    freq = {}
    for x in word:
        freq[x] = freq.get(x,0) + 1
    return freq

def playhand(hand,word_list,totalscore):
    print("these are the hand letters ")
    print(hand)
    word=list()
    word=raw_input("tell a word")
    if word==".":
        return totalscore
    else:
        if len(hand==1):
            return totalscore
        else:
            isthere=is_validword(word,hand,wordlist)
            if isthere==True :
                score=get_word_score(word,n)
                totalscore=totalscore+score
                newhand=update_hand(hand,word)
            playhand(newhand,word_list,totalscore)

def update_hand(hand,word):
    num=get_frequency_dict(word)
    new=num.keys()
    for i in new :
        hand[i]=hand[i]-num[i]
        if hand[i]==0:
            del hand[i]

    return hand
nex=update_hand(hand,word)
print(nex)

def is_validword(word,hand,word_list):
    if all(x in hand.keys() for x in word) and word in word_list:
        print("it is present in the hand and it is a validword")
        return True
    return False



def deal_hand(n,VOWELS,CONSONANTS,SCRABBLE_LETTER_VALUES):
    hand = {}
    num_vowels = n / 3
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = SCRABBLE_LETTER_VALUES.get(x, 0)
    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = SCRABBLE_LETTER_VALUES.get(x, 0)
    return hand

def getwordscore(word,hand):
    valid=get_frequency_dict(word)
    temp=0
    for i in word :
        temp=temp+valid[i]*hand[i]
    if cmp(valid.keys(),hand.keys())==0:
        temp=temp+50
    print(temp)
    return temp
getwordscore(word,hand)

def playgame(word_list):
    totalscore=0
    n=raw_input("enter the size of the hand")
while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(n,VOWELS,CONSONANTS,SCRABBLE_LETTER_VALUES)
            totalscore=playhand(hand.copy(), word_list)
            print(totalscore)
        elif cmd == 'r':
            totalscore=playhand(hand.copy(), word_list)
            print(totalscore)
        elif cmd == 'e':
            break
        else:
             print "Invalid command."
