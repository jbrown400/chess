""" Initializes everything """


""" Imports """
from board import board
from player import player
from game import Game


""" Starting inits """
board = board.Board()
playerW = player.Player("white")
playerB = player.Player("black")
game = Game({"white": playerW, "black": playerB}, board)

""" Starting output """
print("Let's play chess! \n White goes first")
game.turn()
