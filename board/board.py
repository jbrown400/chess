""" A class to represent the board and the history of its states """


class Board():

    state = []
    state_history = []

    def __init__(self):
        self.state = [["\u25A2" for j in range(8)] for i in range(8)]

    def state_change(self):
        pass

    def print_board(self, playerW, playerB):
        count = 1
        print("  a b c d e f g h")
        for row in self.state:
            print(count, end=" ")
            for col in row:
                print(col, end=" ")
            print(count)
            count += 1
        print("  a b c d e f g h")
