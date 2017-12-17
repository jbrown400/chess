""" Functionality for the King piece """


class King():


    """ Initialization """
    def __init__(self, color, location):
        self.color = color
        self.location = location
        self.symbol = ("\u2654" if self.color == "black" else "\u265a")


    """ Move King """
    def move(self):
        pass
