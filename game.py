""" Handles the overall game functionality """

class Game():

    def __init__(self, players, board):
        self.players = players
        self.board = board

    def turn(self):
        self.board.print_board(self.players["white"], self.players["black"])
