import random
import string


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
n=7

VOWELS ="aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def playhand(hand,word_list):
    print("these are the hand letters ")
    print(hand)
    word=list[]
    word=raw_input("tell a word")
    if word==".":
        return
    elif:
        len(hand)==1
        return
    else :
        isthere=is_validword(word,hand,wordlist)
        if isthere==True :
            get_word_score(word,n)
            hand=update_hand(hand,word)
        playhand(hand,word_list)

def update_hand(hand,word):



def is_validword(word,hand,word_list):
    for i in len(word) :
        flag==0
        if word[i] in hand.keys():
            flag==1
        else :
            print("this letter is not there in the hand")
        if flag==0:
            return false
    if word in word_list :
        print("it is a valid word ")
        return true
    else :
        print("its not there in the dictionary")
        return false



def deal_hand(n,VOWELS,CONSONANTS,SCRABBLE_LETTER_VALUES):
    hand = {}
    num_vowels = n / 3
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = SCRABBLE_LETTER_VALUES.get(x, 0)
    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = SCRABBLE_LETTER_VALUES.get(x, 0)
    print(hand)
    return hand



def getwordscore(word,n,hand):
    sum=list()
    temp=0
    for i in word :
        if i in SCRABBLE_LETTER_VALUES :
            sum.append([i])
            temp=temp+(SCRABBLE_LETTER_VALUES[i])
    print(sum)
    print(temp)



def playgame(word_list):
    ch=raw_input("NEW GAME:")
    hand=deal_hand(n,VOWELS,CONSONANTS)
    if ch==n :
        playhand(hand,word_list)
