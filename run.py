""" Initializes everything """

""" Import libraries """
import sys, pygame


""" Import Classes """
from board import board
from player import player
from game import Game


""" Starting inits """
board = board.Board()
playerW = player.Player("white")
playerB = player.Player("black")
game = Game({"white": playerW, "black": playerB}, board)

""" Starting output """
"""
print("Let's play chess! \n White goes first")
while(playerW.lost != False or playerB.lost != False):
    game.turn()
    playerW.lost = True
"""

size = (600, 600)
screen = pygame.display.set_mode(size)
board = pygame.image.load("images/board.jpg")
board = pygame.transform.scale(board, (600, 600))

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()
    screen.blit(board, (0,0))
    pygame.display.flip()
