""" Handles the overall game functionality """

class Game():

    white_move = None
    black_move = None
    valid_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    valid_numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]

    def __init__(self, players, board):
        self.players = players
        self.board = board

    def turn(self):
        # self.board.print_board(self.players["white"], self.players["black"])
        self.board.print_board(self.players)

        # Get user input from the white player
        while(not self.validate_input(input("White move: "))):
            pass
        # Get user input from the black player

    def validate_input(self, move):
        print("Validating move: " + move)
        if(len(move) != 2):
            print("Invalid length for a move")
            return False
        elif(move[0] not in self.valid_letters):
            print("Invalid letter for move")
            return False
        elif(move[1] not in self.valid_numbers):
            print("Invalid number for move")
            return False
        else:
            return True
