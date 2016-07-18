
def is_validword(word,hand,word_list):
    if all(x in hand.keys() for x in word) and word in word_list:
        print("it is present in the hand and it is a validword")
        return True
    return False


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
                return bestchoice(dicc, hand, wordlen, word_list)
    else:
        if len(dicc.keys()) > 0:
            return bestchoice(dicc, hand, wordlen-1, word_list)
        else:
            defaultword = "."
            print("sorry i dont know")
            return defaultword
