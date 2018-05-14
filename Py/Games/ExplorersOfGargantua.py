'''
ExplorersOfGargantua.py
By Aaron Aikman
Decides character stats based upon inputted descriptors
Must be real words
Get some kind of bonus for shorter words vs longer words



'''

from __future__ import division
import string

class Explorer(object):
    def __init__(self, name = 'Dave', race = 'Human', role = 'Warrior'):
        self.race = race
        self.role = role
        self.name = name
        self.evalStats()


    def evalStats(self):
        #Testing for character Happiness
        wordlengths = [len(self.role), len(self.race), len(self.name)]
        allchars = self.role.lower() + self.race.lower() + self.name.lower()
        self.happiness = self.isHappyChar(allchars)

        # Size is the number of chars squared, reduced from cm to m
        self.size = (len(allchars)**2)/100.0

        # Speed is inverse of size multiplied by 1 plus the number of words shorter than 4 chars
        self.speed = (1/self.size) * (1 + (sum([ 1 for i in wordlengths if i < 5])))



    def isHappyChar(self, letters):
        '''
        Happiness is detirmined by the number of characters in the descriptors
        that have an alphabet index that is a happy number
        w a g j m s are happy letters
        TODO Just make it check for letters
        '''
        print letters
        happinessCount = 0
        for char in letters:
            charVal = string.lowercase.index(char) + 1
            if self.isHappyNum(charVal):
                happinessCount += 1
        return happinessCount

    def isHappyNum(self, num, triesRem = 30):
        triesRem -= 1
        sum = 0
        for i in str(num):
            sum += int(i)**2
        if sum == 1:
            return True
        elif triesRem == 0:
            return False
        else:
            return self.isHappyNum(sum, triesRem)

me = Explorer(name = 'hank')
print me.speed
