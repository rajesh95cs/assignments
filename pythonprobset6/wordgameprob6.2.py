import random
import string
import time


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
nex={}
hand={}
score=0
VOWELS ="aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
word=list()
word_list=list()
newhand={}
totaltime=0
starttime=0
endtime=0
subtime=0
enteredword=list()

def load_words():
    print "Loading word list from file..."
    inFile = open("words.txt", 'r', 0)
    wordsa = list()
    for line in inFile:
        wordsa.append(line.strip().lower())
    print "  ", len(wordsa), "words loaded."
    return wordsa

def get_frequency_dict(word):
    freq = {}
    for x in word:
        freq[x] = freq.get(x,0) + 1
    return freq

def playhand(hand,word_list,totalscore,totaltime,timelimit,enteredword):
    print("these are the hand letters ")
    print(hand)
    starttime=time.time()
    word=raw_input("tell a word ")
    endtime=time.time()
    subtime=endtime-starttime
    if subtime>=timelimit :
        print("time over to enter the letter , word not accepted")
        return totalscore
    totaltime = totaltime+subtime
    if word in enteredword:
        print("you are cheating gameover")
        return totalscore
    else :
        if totaltime>=timelimit:
            print("time is over no score provided for the previous word")
            exceededtime=totaltime-timelimit
            print("totaltime taken ",totaltime)
            print("exceededtime =", exceededtime)
            return totalscore
        else:
            print("it took ", subtime ," seconds to get the word")
            enteredword.append(word)
    if word==".":
        return totalscore
    else:
        if len(hand)==1:
            return totalscore
        else:
            isthere=is_validword(word,hand,word_list)
            if isthere==True :
                score=getwordscore(word,hand,subtime)
                print("sub score= ", score)
                totalscore=totalscore+score
                print("totalscore= ", totalscore)
                hand=update_hand(hand,word)
            return playhand(hand,word_list,totalscore,totaltime,timelimit,enteredword)

def update_hand(hand,word):
    num=get_frequency_dict(word)
    new=num.keys()
    for i in new :
        hand[i]=hand[i]-num[i]
        if hand[i]==0:
            del hand[i]

    return hand

def is_validword(word,hand,word_list):
    if all(x in hand.keys() for x in word) and word in word_list:
        print("it is present in the hand and it is a validword")
        return True
    return False



def deal_hand(N,VOWELS,CONSONANTS,SCRABBLE_LETTER_VALUES):
    num_vowels=N/3
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = SCRABBLE_LETTER_VALUES.get(x, 0)+1
    for i in range(num_vowels, N):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = SCRABBLE_LETTER_VALUES.get(x, 0)+1
    return hand

def getwordscore(word,hand,subtime):
    valid=get_frequency_dict(word)
    temp=0
    for i in word :
        temp=temp+valid[i]*hand[i]
    if cmp(valid.keys(),hand.keys())==0:
        temp=temp+50
    temp=temp/subtime
    return temp

def playgame(word_list):
    totscore=0
    totalscore=0
    while True:
        timelimit=int(raw_input("enter the time limit : "))
        N=int(raw_input("enter the size of the hand"))
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(N,VOWELS,CONSONANTS,SCRABBLE_LETTER_VALUES)
            totscore=playhand(hand.copy(), word_list,totalscore,totaltime,timelimit,enteredword)
            print(totscore)
        elif cmd == 'r':
            totscore=playhand(hand.copy(), word_list,totalscore,totaltime,timelimit,enteredword)
            print(totscore)
        elif cmd == 'e':
            break
        else:
             print "Invalid command."
word_list=load_words()
playgame(word_list)
