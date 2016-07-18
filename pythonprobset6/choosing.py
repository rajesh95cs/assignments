
def is_validword(word,hand,word_list):
    if all(x in hand.keys() for x in word) and word in word_list:
        print("it is present in the hand and it is a validword")
        return True
    return False

def bestchoice(dicc,hand,word_list):
    if len(hand.keys()) in dicc.keys():
        maxscore=max(dicc[len(hand.keys())].keys())
        word=dicc[len(hand.keys())][maxscore][random.randrange(0,len(dicc[len(hand.keys())][max]))]
        if is_validword(word,hand,word_list):
            return word
        else:
            bestchoice(dicc,hand,word_list)
    else :
        defaultword="."
        print("sorry i dont know")
        return defaultword            
