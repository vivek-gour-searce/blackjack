__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2013, Searce'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Vivek.Gour@searce.com'
__status__ = 'Development'

from random import randrange
import Tkinter
import tkMessageBox
from Tkinter import *
startGame = Tkinter.Tk(className="Black-Jack Game")


class myNewGame(object):
    # __slots__ = ['deck', 'playGameObj']

    def __init__(self):
        self.deck = ['A', 'J', 'Q', 'K', '2', '3', '4', '5', '6', '7', '8', '9', '10'] * 4 * 6
        self.playerScore = []
        self.dealerScore = []
        b1 = Button(startGame, text="Start Game", command=self.playBlackJackGame)
        b1.pack()
        b1.place(height=30, width=80, x=60, y=80)
        startGame.minsize(width=200, height=200)
        startGame.mainloop()

    def playBlackJackGame(self):
        startGame.destroy()
        self.playGame = Tkinter.Tk(className="Black-Jack Game")
        self.playerCards = StringVar()
        self.dealerCards = StringVar()
        self.playerPoints = StringVar()
        self.dealerPoints = StringVar()
        l1 = Label(self.playGame, text="Player")
        l2 = Label(self.playGame, text="Dealer")
        l3 = Label(self.playGame, textvariable=self.playerCards)
        l4 = Label(self.playGame, textvariable=self.dealerCards)
        l5 = Label(self.playGame, textvariable=self.playerPoints)
        l6 = Label(self.playGame, textvariable=self.dealerPoints)
        self.playerCards.set(" ")
        self.dealerCards.set(" ")
        l1.pack()
        l1.place(height=30, width=80, x=50, y=30)
        l2.pack()
        l2.place(height=30, width=80, x=280, y=30)
        l3.pack()
        l3.place(height=30, width=200, x=50, y=70)
        l4.pack()
        l4.place(height=30, width=200, x=280, y=70)
        l5.pack()
        l5.place(height=30, width=80, x=50, y=10)
        l6.pack()
        l6.place(height=30, width=80, x=280, y=10)
        self.b3 = Tkinter.Button(self.playGame, text="Deal", command=self.deal)
        self.b3.pack()
        self.b3.place(height=30, width=80, x=100, y=150)

        self.playGame.minsize(width=500, height=200)
        self.playGame.mainloop()

    def getCardPoint(self, cards):
        cardpoints = 0
        for card in cards:
            if card in ['A']:
                cardpoints += 11
            elif card in ['J', 'Q', 'K']:
                cardpoints += 10
            else:
                cardpoints += 1
        return cardpoints

    def deal(self):
        self.b3.destroy()
        self.playGame.minsize(width=500, height=200)
        self.userCards = [self.drawCards(), self.drawCards()]
        self.systemCards = [self.drawCards()]
        self.playerCards.set(" | ".join(self.userCards))
        self.dealerCards.set(" | ".join(self.systemCards))
        self.userPoints = self.getCardPoint(self.userCards)
        self.systemPoints = self.getCardPoint(self.systemCards)
        self.playerPoints.set(self.userPoints)
        self.dealerPoints.set(self.systemPoints)
        self.getResult()

    def getResult(self):
        if self.userPoints > 21:
            self.b1.destroy()
            self.b2.destroy()
            self.b3 = Tkinter.Button(self.playGame, text="Deal Again", command=self.deal)
            self.b3.pack()
            self.b3.place(height=30, width=80, x=280, y=150)
            self.b4 = Tkinter.Button(self.playGame, text="Statistic", command=self.statistics)
            self.b4.pack()
            self.b4.place(height=30, width=80, x=400, y=150)
            self.lose("Player")
            self.playerScore.append(self.userPoints)
            self.dealerScore.append(self.systemPoints)
        elif self.userPoints < 21:
            self.b1 = Tkinter.Button(self.playGame, text="Pick a Card", command=self.pickCard)
            self.b2 = Tkinter.Button(self.playGame, text="Skip", command=self.skip)
            self.b1.pack()
            self.b1.place(height=30, width=80, x=280, y=150)
            self.b2.pack()
            self.b2.place(height=30, width=80, x=400, y=150)
        else:
            self.b1.destroy()
            self.b2.destroy()
            self.b3 = Tkinter.Button(self.playGame, text="Deal Again", command=self.deal)
            self.b3.pack()
            self.b3.place(height=30, width=80, x=280, y=150)
            self.b4 = Tkinter.Button(self.playGame, text="Statistic", command=self.statistics)
            self.b4.pack()
            self.b4.place(height=30, width=80, x=400, y=150)
            self.won("Player")
            self.playerScore.append(self.userPoints)
            self.dealerScore.append(self.systemPoints)

    def pickCard(self):
        self.b3.destroy()
        self.userCards.append(self.drawCards())
        self.playerCards.set(" | ".join(self.userCards))
        self.userPoints = self.getCardPoint(self.userCards)
        self.playerPoints.set(self.userPoints)
        self.getResult()

    def skip(self):
        self.b3.destroy()
        self.systemCards.append(self.drawCards())
        self.dealerCards.set(" | ".join(self.systemCards))
        self.systemPoints = self.getCardPoint(self.systemCards)
        self.dealerPoints.set(self.systemPoints)
        if self.systemPoints == 21:
            self.b1.destroy()
            self.b2.destroy()
            self.b3 = Tkinter.Button(self.playGame, text="Deal Again", command=self.deal)
            self.b3.pack()
            self.b3.place(height=30, width=80, x=280, y=150)
            self.b4 = Tkinter.Button(self.playGame, text="Statistic", command=self.statistics)
            self.b4.pack()
            self.b4.place(height=30, width=80, x=400, y=150)
            self.won("Dealer")
            self.playerScore.append(self.userPoints)
            self.dealerScore.append(self.systemPoints)
        elif self.systemPoints <= 16:
            self.skip()
        elif self.systemPoints >= 17:
            self.finalResult()

    def finalResult(self):
        if self.systemPoints >= 17 and self.userPoints < 21:

            if self.userPoints > self.systemPoints:
                self.won("Player")
                self.b3 = Tkinter.Button(self.playGame, text="Deal Again", command=self.deal)
                self.b3.pack()
                self.b3.place(height=30, width=80, x=280, y=150)
            else:
                self.won("Dealer")
                self.b3 = Tkinter.Button(self.playGame, text="Deal Again", command=self.deal)
                self.b3.pack()
                self.b3.place(height=30, width=80, x=280, y=150)
            self.playerScore.append(self.userPoints)
            self.dealerScore.append(self.systemPoints)
            self.playerPoints.set(self.userPoints)
            self.dealerPoints.set(self.systemPoints)

    def statistics(self):

        l1 = Label(self.playGame, text="Statistics")
        l1.pack()
        l1.place(height=30, width=80, x=20, y=230)
        Games = StringVar()
        l2 = Label(self.playGame, text="Games", textvariable=Games)
        l2.pack()
        l2.place(height=30, width=500, x=20, y=260)
        Games.set(" | ".join(["Game %s" % (x) for x in range(1,len(self.playerScore)+1)]))
        Player = StringVar()
        l3 = Label(self.playGame, text="Player", textvariable=Player)
        l3.pack()
        l3.place(height=30, width=500, x=20, y=290)
        Player.set(" | ".join(map(lambda x: "    "+str(x)+"    ", self.playerScore)))
        Dealer = StringVar()
        l4 = Label(self.playGame, text="Dealer", textvariable=Dealer)
        l4.pack()
        l4.place(height=30, width=500, x=20, y=320)
        Dealer.set(" | ".join(map(lambda x: "    "+str(x)+"    ", self.dealerScore)))
        self.playGame.minsize(width=500, height=400)

    def won(self, user):
        tkMessageBox.showinfo("WON !!", user+" Won The Game")

    def lose(self, user):
        tkMessageBox.showinfo("LOSE !!", user+" Lose The Game")

    def drawCards(self):
        return self.deck[randrange(0, 311)]


if __name__ == "__main__":
    g = myNewGame()