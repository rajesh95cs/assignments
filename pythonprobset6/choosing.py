import random
import string


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


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
    if wordlen in dicc.keys():
        maxscore = max(dicc[wordlen].keys())
        print "maxscore = ", maxscore
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
        if len(dicc.keys()) > 0 and wordlen > 2:
            return bestchoice(dicc, hand, wordlen-1, word_list)
        else:
            defaultword = "."
            print("sorry i dont know")
            return defaultword


word_list = load_words()
dicc = pointdict(word_list)
hand = {'d': 1, 'b': 1, 'f': 1}
# print dicc
print bestchoice(dicc, hand, sum(hand.values()), word_list)
