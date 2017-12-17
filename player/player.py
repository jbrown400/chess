""" Player functionality """

from pieces.king import King
# import pieces.king.King

class Player():

    def __init__(self):
        self.my_turn = False
        self.in_check = False
        self.lost = False
        self.pieces = []
        self.init_pieces()

    """ Move a piece that belongs to that player """
    def move(self, piece, location):
        pass

    """ Add a piece to the player's collection """
    def generate_piece(piece):
        pass

    """ Initialize pieces for the start of the game """
    def init_pieces(self):
        self.pieces.append(King("black", "a5"))
