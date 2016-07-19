import random
import string
import time


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 1, 'c': 1, 'd': 2, 'e': 1, 'f': 2, 'g': 1, 'h': 2, 'i': 1,
    'j': 2, 'k': 2, 'l': 1, 'm': 2, 'n': 1, 'o': 1, 'p': 2, 'q': 2, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 2, 'w': 1, 'x': 2, 'y': 2, 'z': 2
}
wordlen = 0
nex = {}
hand = {}
score = 0
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
word = list()
word_list = list()
newhand = {}
totaltime = 0
starttime = 0
endtime = 0
subtime = 0
enteredword = list()
locdict = {}



def get_frequency_dict(word):
    freq = {}
    for x in word:
        freq[x] = freq.get(x, 0) + 1
    return freq


def getwordmaxscore(word, SCRABBLE_LETTER_VALUES):
    valid = get_frequency_dict(word)
    temp = 0
    for i in word:
        temp = temp+valid[i]*SCRABBLE_LETTER_VALUES[i]
    return temp


def load_words():
    print "Loading word list from file..."
    inFile = open("words.txt", 'r', 0)
    wordsa = list()
    for line in inFile:
        wordsa.append(line.strip().lower())
    print "  ", len(wordsa), "words loaded."
    return wordsa


def pointdict(word_list):
    dicc = {}
    for i in range(len(word_list)):
        lenword = len(word_list[i])
        word = word_list[i]
        wordmaxscore = getwordmaxscore(word, SCRABBLE_LETTER_VALUES)
        if lenword not in dicc.keys():
            dicc[lenword] = {wordmaxscore: [word]}
        else:
            if wordmaxscore not in dicc[lenword].keys():
                dicc[lenword][wordmaxscore] = [word]
            else:
                dicc[lenword][wordmaxscore].append(word)
    return dicc


def is_validword(word, hand, word_list):
    word_freq = get_frequency_dict(word)
    if all(key in hand.keys() and word_freq[key] <= hand[key] for key in word_freq) and word in word_list:
        print("it is present in the hand and it is a validword")
        return True
    return False


def bestchoice(dicc, hand, wordlen, word_list):
    print "wordlen = ", wordlen
    while wordlen > 1:
        #print ("hi")
        while len(dicc[wordlen].keys()) != 0:
            #print("hello")
            maxscore = max(dicc[wordlen].keys())
            for word in dicc[wordlen][maxscore]:
                #print("is it working")
                if is_validword(word, hand, word_list):
                    print(word)
                    return word
                else:
                    dicc[wordlen][maxscore].remove(word)
            del dicc[wordlen][maxscore]
        del dicc[wordlen]
        wordlen = wordlen - 1
        print wordlen
    defaultword = "."
    print("sorry no word known")
    return defaultword


def playhand(hand, word_list, totalscore,enteredword,
             dicc):
    print("these are the hand letters ")
    print(hand)
    wordlen=sum(hand.values())
    word = bestchoice(dicc, hand, wordlen, word_list)
    if word in enteredword:
        print("you are cheating gameover")
        return totalscore
    else:
        enteredword.append(word)
    if word == ".":
        return totalscore
    else:
        if len(hand) == 1:
            return totalscore
        else:
            isthere = is_validword(word, hand, word_list)
            if isthere:
                score = getwordscore(word, hand)
                print("sub score= ", score)
                totalscore = totalscore+score
                print("totalscore= ", totalscore)
                hand = update_hand(hand, word)
            return playhand(hand, word_list, totalscore,
                            enteredword, dicc)


def update_hand(hand, word):
    num = get_frequency_dict(word)
    new = num.keys()
    for i in new:
        hand[i] = hand[i]-num[i]
        if hand[i] == 0:
            del hand[i]
    return hand




def deal_hand(N, VOWELS, CONSONANTS, SCRABBLE_LETTER_VALUES):
    num_vowels = N/3
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = SCRABBLE_LETTER_VALUES.get(x, 0)+1
    for i in range(num_vowels, N):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = SCRABBLE_LETTER_VALUES.get(x, 0)+1
    return hand


def getwordscore(word, hand):
    valid = get_frequency_dict(word)
    temp = 0
    for i in word:
        temp = temp+valid[i]*hand[i]
    if cmp(valid.keys(), hand.keys()) == 0:
        temp = temp+50

    return temp

def playgame(word_list):
    totscore = 0
    totalscore = 0
    while True:
        N = int(raw_input("enter the size of the hand"))
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand,\
                                 or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(N, VOWELS, CONSONANTS, SCRABBLE_LETTER_VALUES)
            totscore = playhand(hand.copy(), word_list, totalscore,enteredword, dicc)
            print(totscore)
        elif cmd == 'r':
            totscore = playhand(hand.copy(), word_list, totalscore,enteredword, dicc)
            print(totscore)
        elif cmd == 'e':
            break
        else:
            print "Invalid command."
dicc = {}
word_list = load_words()
dicc = pointdict(word_list)
playgame(word_list)
