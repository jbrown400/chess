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
        
        # Loop until someone loses
        while(self.players["white"].lost != True or self.players["black"].lost != True):
            self.board.print_board(self.players)
            
            # Get user input from the white player
            print("White move: ", end="")
            self.white_move = self.validate_input()
            print(self.white_move)
            # while(not self.validate_input(input("White move: "))):
            #    pass

            if(self.players["white"].lost == True):
                continue

            # Get user input from the black player
            print("Black move: ", end="")
            self.black_move = self.validate_input()
            print(self.black_move)

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
