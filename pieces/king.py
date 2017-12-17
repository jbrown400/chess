""" Functionality for the King piece """


class King():


    """ Initialization """
    def __init__(self, color, location, owner):
        self.color = color
        self.location = location
        self.symbol = ("\u265a" if self.color == "black" else "\u2654")
        self.owner = owner


    """ Move King """
    def move(self):
        pass
