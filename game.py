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
        # Loop until someone loses
        while(self.players["white"].lost != True or self.players["black"].lost != True):
            self.board.print_board(self.players)
            # Get user input from the white player
            print("White pieces:\n------")
            self.players["white"].print_pieces()
            print("White move: ", end="")
            self.white_move = self.validate_input()

            if(self.players["white"].lost == True):
                continue

            self.board.print_board(self.players)
            # Get user input from the black player
            print("Black pieces:\n------")
            self.players["black"].print_pieces()
            print("Black move: ", end="")
            self.black_move = self.validate_input()

            if(self.players["black"].lost == True):
                continue

        if(self.players["white"].lost == False):
            print("White wins!")
        else:
            print("Black wins!")

    def validate_input(self):
        while(True):
            move = input()
            if(len(move) != 2):
                print("Invalid length for a move")
            elif(move[0] not in self.valid_letters):
                print("Invalid letter for move")
            elif(move[1] not in self.valid_numbers):
                print("Invalid number for move")
            else:
                return move
            print("Try again: ", end="")
