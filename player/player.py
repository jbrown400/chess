""" Player functionality """

from pieces.king import King
# import pieces.king.King

class Player():

    def __init__(self, color):
        self.my_turn = False
        self.in_check = False
        self.lost = False
        self.color = color
        self.pieces = []
        self.init_pieces()

    """ Move a piece that belongs to that player """
    def move(self, piece, location):
        pass

    """ 
        Add a piece to the player's collection
        Takes a string value to tell which type of piece to generate.
    """
    def generate_piece(self, piece):
        pass

    def print_pieces(self):
        for piece in self.pieces:
            print(piece.name + ": " + piece.location)

    """ Initialize pieces for the start of the game """
    def init_pieces(self):
        self.pieces.append(King(self.color, "e8" if self.color == "black" else "e1", self))
