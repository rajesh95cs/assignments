import random
import string
import time


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
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
        freq[x] = freq.get(x, 0) + 1
    return freq


def bestchoice(dicc, hand, wordlen, word_list):
    if wordlen in dicc.keys():
        maxscore = max(dicc[wordlen].keys())
        i = random.randrange(0, len(dicc[wordlen][maxscore]))
        word = dicc[wordlen][maxscore][i]
        if is_validword(word, hand, word_list):
            return word
        else:
            del dicc[wordlen][maxscore][i]
            if len(dicc[wordlen][maxscore]) > 0:
                return bestchoice(dicc, hand, wordlen, word_list)
            else:
                del dicc[wordlen][maxscore]
                if len(dicc[wordlen].keys()) == 0:
                    del dicc[wordlen]
                return bestchoice(dicc, hand, wordlen, word_list)
    else:
        if len(dicc.keys()) > 0:
            return bestchoice(dicc, hand, wordlen-1, word_list)
        else:
            defaultword = "."
            print("sorry i dont know")
            return defaultword


def playhand(hand, word_list, totalscore, totaltime, timelimit, enteredword,
             dicc):
    print("these are the hand letters ")
    print(hand)
    starttime = time.time()
    wordlen = sum(hand.values())
    word = bestchoice(dicc, hand, wordlen, word_list)
    endtime = time.time()
    subtime = endtime-starttime
    if subtime >= timelimit:
        print("time over to enter the letter , word not accepted")
        return totalscore
    totaltime = totaltime+subtime
    if word in enteredword:
        print("you are cheating gameover")
        return totalscore
    else:
        if totaltime >= timelimit:
            print("time is over no score provided for the previous word")
            exceededtime = totaltime-timelimit
            print("totaltime taken ", totaltime)
            print("exceededtime =", exceededtime)
            return totalscore
        else:
            print("it took ", subtime, " seconds to get the word")
            enteredword.append(word)
    if word == ".":
        return totalscore
    else:
        if len(hand) == 1:
            return totalscore
        else:
            isthere = is_validword(word, hand, word_list)
            if isthere:
                score = getwordscore(word, hand, subtime)
                print("sub score= ", score)
                totalscore = totalscore+score
                print("totalscore= ", totalscore)
                hand = update_hand(hand, word)
            return playhand(hand, word_list, totalscore, totaltime, timelimit,
                            enteredword, dicc)


def update_hand(hand, word):
    num = get_frequency_dict(word)
    new = num.keys()
    for i in new:
        hand[i] = hand[i]-num[i]
        if hand[i] == 0:
            del hand[i]
    return hand


def is_validword(word, hand, word_list):
    if all(x in hand.keys() for x in word) and word in word_list:
        print("it is present in the hand and it is a validword")
        return True
    return False


def deal_hand(N, VOWELS, CONSONANTS, SCRABBLE_LETTER_VALUES):
    num_vowels = N/3
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = SCRABBLE_LETTER_VALUES.get(x, 0)+1
    for i in range(num_vowels, N):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = SCRABBLE_LETTER_VALUES.get(x, 0)+1
    return hand


def getwordscore(word, hand, subtime):
    valid = get_frequency_dict(word)
    temp = 0
    for i in word:
        temp = temp+valid[i]*hand[i]
    if cmp(valid.keys(), hand.keys()) == 0:
        temp = temp+50
    temp = temp/subtime
    return temp


def getwordmaxscore(word, SCRABBLE_LETTER_VALUES):
    valid = get_frequency_dict(word)
    temp = 0
    for i in word:
        temp = temp+valid[i]*SCRABBLE_LETTER_VALUES[i]
    return temp


def pointdict(word_list):
    for i in range(len(word_list)):
        lenword = len(word_list[i])
        word = word_list[i]
        wordmaxscore = getwordmaxscore(word, SCRABBLE_LETTER_VALUES)
        if lenword not in dicc.keys():
            dicc[lenword] = {wordmaxscore: [word]}
        else:
            if score not in dicc[lenword].keys():
                dicc[lenword][wordmaxscore] = [word]
            else:
                dicc[lenword][wordmaxscore].append(word)
    return dicc


def playgame(word_list, locdict):
    totscore = 0
    totalscore = 0
    while True:
        timelimit = int(raw_input("enter the time limit : "))
        N = int(raw_input("enter the size of the hand"))
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand,\
                                 or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(N, VOWELS, CONSONANTS, SCRABBLE_LETTER_VALUES)
            totscore = playhand(hand.copy(), word_list, totalscore, totaltime,
                                timelimit, enteredword, dicc)
            print(totscore)
        elif cmd == 'r':
            totscore = playhand(hand.copy(), word_list, totalscore, totaltime,
                                timelimit, enteredword, dicc)
            print(totscore)
        elif cmd == 'e':
            break
        else:
            print "Invalid command."
dicc = {}
word_list = load_words()
dicc = pointdict(word_list)
playgame(word_list, locdict)
