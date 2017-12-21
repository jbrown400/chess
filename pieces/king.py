""" Functionality for the King piece """

import pygame

class King():


    """ Initialization """
    def __init__(self, color, location, owner):
        self.color = color
        self.location = location
        if(color == "white"):
            self.image = pygame.image.load("images/white_king.png")
        else:
            self.image = pygame.image.load("images/black_king.png")
        self.owner = owner
        self.name = "King"


    """ Move King """
    def move(self):
        pass
