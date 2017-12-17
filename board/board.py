""" A class to represent the board and the history of its states """


class Board():

    state = []
    state_history = []

    def __init__(self):
        self.state = [["\u25A2" for j in range(8)] for i in range(8)]
        self.x_axis = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
        self.y_axis = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8}

    def state_change(self):
        pass

    def print_board(self, players):
        # Place each players pieces in the state object
        for color, player in players.items():
            for piece in player.pieces:
                x = self.x_axis[piece.location[0]]
                y = self.y_axis[piece.location[1]]
                self.state[y-1][x-1] = piece.symbol

        # Print the board
        count = 1
        print("  a b c d e f g h")
        for row in self.state:
            print(count, end=" ")
            for col in row:
                print(col, end=" ")
            print(count)
            count += 1
        print("  a b c d e f g h")
