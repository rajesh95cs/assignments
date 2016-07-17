import random
import string
randwords=list()
word_list=list()
"""def load_words():
    print "Loading word list from file..."
    inFile = open("words.txt", 'r', 0)
    wordsa = list()
    for line in inFile:
        wordsa.append(line.strip().lower())
    print "  ", len(wordsa), "words loaded."
    return wordsa
word_list=load_words()
for i in range(0,10):
    randwords.append(word_list[random.randrange(0,len(word_list))])
print(randwords)
"""
s={1:{10:["hi"]},2:{20:["hello"]},3:{29:["how is it"]}}
for i in range(len(s)):
    print("length of the dictionary", len(s))
    a=int(raw_input("enter section "))
    num=int(raw_input("enter a number "))
    if a in s.keys():
        print(s.keys()[i])
        if num in s.values()[i].keys():
            print(s.values()[i].keys())
            print s.values()[i].values()
