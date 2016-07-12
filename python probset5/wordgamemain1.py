import random
import string


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
n=7

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

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
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
    for i in len(word):
        if word[i] in hand.keys() and hand[word[i]] != 0:
            hand[word[i]]=hand[word[i]]-1
        else:
            if word[i] in hand.keys() :
                del hand[word[i]]
    return hand

def is_validword(word,hand,word_list):
    for i in len(word) :
        flag==0
        if word[i] in hand.keys() and hand[i]!=0:
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
    return hand

def getwordscore(word,n,hand):
    temp=0
    for i in word :
        if i in hand :
            temp=temp+(hand[i])
    return temp

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
