# Black Jack by Aaron Aikman
# TODO add splitting, doubling, card counting, saying house always wins and betting

import collections
from random import choice
import inspect


Card = collections.namedtuple('Card', ['rank', 'suit'])


class SingleDeck(object):
    ranks = (list(str(n) for n in range(2,11)) + list('JQKA'))
    suits = 'Spades Diamonds Clubs Hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

class BlackJackGame(object):
    def __init__(self, deck):
        self.deck = deck
        self.dealerStay = 17
        self.resetHands()
        self.greet()
        self.deal()


    def greet(self):
        print 'Welcome to Chez Jacques Noire!\nLet the fun begin!'


    def resetHands(self):
        self.playerHand = []
        self.dealerHand = []


    def checkCurrentWinner(self):
        dealerScore = self.checkValue(0)
        playerScore = self.checkValue(1)
        if dealerScore >= playerScore:
            return 0
        else:
            return 1

    def roundEnd(self):
        self.showHands(1)
        if self.checkCurrentWinner():
            print 'You win! {} to {}'.format(self.checkValue(1), self.checkValue(0))
        else:
            print 'Dealer wins. {} to {}'.format(self.checkValue(0), self.checkValue(1))
        self.askToPlayAgain()


    def deal(self):
        self.giveCard(0)
        self.giveCard(1)
        self.giveCard(0)
        self.giveCard(1)
        self.showHands()
        self.playTurn()

    def playTurn(self):
        playerChoice = 1
        while playerChoice:
            playerChoice = raw_input("Hit or Stay?\n")
            if playerChoice.lower() == 'h' or playerChoice.lower() == 'hit':
                self.giveCard(1)
                self.showHands()
                if self.checkValue(1) == 0:
                    playerChoice = 0
                    print 'You bust!'
                    self.roundEnd()
            else:
                self.dealerTurn()
                self.roundEnd()


    def giveCard(self, bPlayer):
        if bPlayer:
            self.playerHand += choice(self.deck)
        else:
            self.dealerHand += choice(self.deck)


    def showHands(self, bShowToPlayer = 0):
        print '\n\nDealer'
        if bShowToPlayer:
            print self.dealerHand
        else:
            print (self.dealerHand[0:2], 'Hidden')
        print '\nPlayer'
        print self.playerHand
        print '\n'


    def checkValue(self, bPlayer):
        pointTotal = 0
        handToCount = []
        if bPlayer:
            handToCount = self.playerHand[::2]
        else:
            handToCount = self.dealerHand[::2]
        numAces = 0
        for card in handToCount:
            if card == 'A':
                numAces += 1
            try:
                pointTotal += int(card)
            except:
                if card != 'A':
                    pointTotal += 10

        # Handling Aces last because of variability
        if numAces == 1:
            if pointTotal < 12:
                pointTotal += 11
            else:
                pointTotal += 1
        else:
            for i in range(numAces):
                if pointTotal < (12 - numAces):
                    pointTotal += 11
                else:
                    pointTotal += 1

        if pointTotal < 22:
            return pointTotal
        else:
            return 0

    def dealerTurn(self):
        # Hit if Dealer has not busted and is either losing or below dealerStay
        while self.checkValue(0) and (self.checkCurrentWinner() or self.checkValue(0) < (self.dealerStay)):
            print '\nDealer hits'
            self.giveCard(0)
        if self.checkValue(0) == 0:
            print '\nDealer busts'
        else:
            print '\nDealer stays'


    def askToPlayAgain(self):
        playAgainChoice = raw_input('\nWould you like to play again?')
        if playAgainChoice.lower() == 'y' or playAgainChoice.lower() == 'yes':
            self.resetHands()
            self.deal()
        else:
            print '\nThank you for playing'
            exit()




d = SingleDeck()

g = BlackJackGame(d)


