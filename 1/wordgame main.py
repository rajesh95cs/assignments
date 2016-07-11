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
    while hand.keys()==".":
        word=raw_input("tell a word")
        isthere=is_validword(word,hand,word_list)
        if isthere==true :
            getwordscore(word,n)
            update(hand,word)
        display_hand(hand)

def deal_hand(n,VOWELS,CONSONANTS):
    hand = {}
    num_vowels = n / 3
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
    print(hand)
    return hand




def playgame(word_list):
    ch=raw_input("NEW GAME:")
    hand=deal_hand(n,VOWELS,CONSONANTS)
    if ch==n :
        playhand(hand,word_list)
