import string
import random as r
import secrets

class password:
    """ 
        Base class 
    """
    def __init__(self):
        """ Variables needed for all child classes """
        self.password = []

    def get(self):
        """ Return the string version of the password """
        if isinstance(self.password, str):
            return self.password
        return "".join(self.password)
    
    def __repr__(self):
        return str(self.password)

    __str__ = __repr__

class passwordRandom(password):
    """
        Creates an n-length password of a random combination of characters
    """
    def __init__(self, length=16, exclude=[]):
        """ Create the basic varaibles """
        self.length = length
        self.exclude = [str(i) for i in exclude]
        self.fullList = self.removeExcluded(self.getFull())
        self.password = self.create()
        


    def getFull(self):
        """ Get the full list of possible characters, filter out any chars that may affect statements """
        full = (string.printable).replace("\"", "")
        full = full.replace("\\", "")
        full = full.replace(" ", "")
        full = full[0:92]

        return full
    
    def removeExcluded(self, arr):
        arr = [str(i) for i in arr]
        a = set(arr)
        b = set(self.exclude)
        new_arr = list(a-b)

        return new_arr

    def create(self):
        """ Generate the password from the full list of available characters """
        password = []
        for _ in range(self.length):
            letter = r.choice(self.fullList)
            password.append(letter)

        return "".join(password)

class passwordWorded(password):
    """
        Creates an random password of a random choice of avaiable words and numbers
    """
    def __init__(self, wordCount=3, numberCount=3):
        """ Create the basic varaibles """
        self.wordCount = wordCount
        self.numberCount = numberCount
        self.password = self.create()

    def getWords(self):
        """ Return a set of the 300,000 words in the text file """
        with open('words.txt') as f:
            words = f.read().split()

        return words

    def getRandomWords(self):
        """ Return a list of words taken from the file"""
        random_sample = []
        words = self.getWords()
        for _ in range(self.wordCount):
            random_sample.append(secrets.choice(words))

        return random_sample
    
    def xRandomNumbers(self, x):
        nums = []
        for _ in range(x):
            nums.append(str(secrets.randbelow(10)))

        return "".join(nums)

    def create(self):
        """ Generate the full password from the random words and numbers """
        contents = self.getRandomWords()

        for _ in range(self.numberCount):
            contents.append(self.xRandomNumbers(3))

        r.shuffle(contents)
        password = "_".join(contents)
        
        return password

    

