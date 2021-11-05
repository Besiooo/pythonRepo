import math
import random


class Player:
    def __init__(self, letter):
        # letter --> X or O, player's choice
        self.letter = letter

        # all players get their move
        def get_move(self, game):
            pass


class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #   get a random available square AI can fill with its mark
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        __valid_square = False  # this is just a check that won't let invalid inuts through
        value = None  # this stores the index of player's choice to put a mark on

        while not __valid_square:
            square = input(self.letter + "'s move! [0 - 8] --> ")
            try:
                value = int(square)  # check 1: is this input an integer?
                if value not in game.available_moves():
                    raise ValueError  # game says "hey, this input is invalid!'
                __valid_square = True  # yay, it passed the tests!
            except ValueError:
                print("Oops, wrong value - try again!")

        return value

