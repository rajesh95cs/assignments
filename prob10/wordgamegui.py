class Hand(object):
    def __init__(self, handSize, initialHandDict = None):
        """
        Initialize a hand.

        handSize: The size of the hand

        postcondition: initializes a hand with random set of initial letters.
        """
        num_vowels = handSize / 3
        if initialHandDict is None:
            initialHandDict = {}
            for i in range(num_vowels):
                x = VOWELS[random.randrange(0,len(VOWELS))]
                initialHandDict[x] = initialHandDict.get(x, 0) + 1
            for i in range(num_vowels, handSize):
                x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
                initialHandDict[x] = initialHandDict.get(x, 0) + 1
        self.initialSize = handSize
        self.handDict = initialHandDict
    def update(self, word):
        """
        Remove letters in word from this hand.

        word: The word (a string) to remove from the hand
        postcondition: Letters in word are removed from this hand
        """

        num=get_frequency_dict(word)
        new=num.keys()
        for i in new :
            self.handDict[i]=self.handDict[i]-num[i]
            if self.handDict[i]==0:
                del self.handDict[i]


        # TODO
    def containsLetters(self, letters):
        """
        Test if this hand contains the characters required to make the input
        string (letters)

        returns: True if the hand contains the characters to make up letters,
        False otherwise
        """
        letterfreq= get_frequency_dict(letters)
        return all(key in self.handDict.keys() and letterfreq[key] <= self.handDict[key] for key in letterfreq

        # TODO
    def isEmpty(self):
        """
        Test if there are any more letters left in this hand.

        returns: True if there are no letters remaining, False otherwise.
        """
        if len(self.handDict) == 0 :
            return True
        else :
            return False



        # TODO
    def __iter__(self):
        return iter(self.handDict)
    def __eq__(self, other):
        """
        Equality test, for testing purposes

        returns: True if this Hand contains the same number of each letter as
        the other Hand, False otherwise
        """
        return type(other) == Hand and all(key in self.handDict.keys() and other.handDict[key] == self.handDict[key]) for key in other
        # TODO
    def __str__(self):
        """
        Represent this hand as a string

        returns: a string representation of this hand
        """
        string = ''
        for letter in self.handDict.keys():
            for j in range(self.handDict[letter]):
                string = string + letter + ' '
        return string
def get_frequency_dict(word):
    freq = {}
    for x in word:
    freq[x] = freq.get(x,0) + 1
    return freq
