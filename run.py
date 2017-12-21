""" Initializes everything """

""" Import libraries """
import sys, pygame


""" Import Classes """
from board import board
from player import player
from game import Game


""" Init All The Things! """
# Declarations of game objects
board = board.Board()
playerW = player.Player("white")
playerB = player.Player("black")
game = Game({"white": playerW, "black": playerB}, board)

# Constants
START_X = 60
START_Y = 50
ADJUST = 110

""" Starting output """
"""
print("Let's play chess! \n White goes first")
while(playerW.lost != False or playerB.lost != False):
    game.turn()
    playerW.lost = True
"""

screen_size = (1000, 1000)
screen = pygame.display.set_mode(screen_size)
field_size = (800, 800)
# field = pygame.display.set_mode(field_size)
board = pygame.image.load("images/board.jpg")
board = pygame.transform.scale(board, (1000, 1000))
king = pygame.image.load("images/black_king.png")
king = pygame.transform.scale(king, (100, 100))

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()
    screen.blit(board, (0,0))
    screen.blit(king, (60, 50))
    screen.blit(king, (60 + ADJUST, 50))
    screen.blit(king, (60 + (ADJUST * 7), 50))
    screen.blit(king, (60, 50 + ADJUST))
    screen.blit(king, (60, 50 + (ADJUST * 7)))
    screen.blit(king, (60 + (ADJUST * 7), 50 + (ADJUST * 7)))
    pygame.display.flip()
