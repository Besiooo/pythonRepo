class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # self.board = self.width * [self.height * [' O ']]
        self.board = [
            [' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O '],
            [' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O '],
            [' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O '],
            [' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O '],
            [' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O '],
            [' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O '],
            [' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O '],
            [' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O '],
            [' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O '],
            [' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ']
        ]

    def show(self):
        for row in range(self.height):
            for col in range(self.width):
                print(self.board[col][row], end='')
            print()

    def show_char(self, c, r):
        print(self.board[c][r])


    def capture(self, c, r):
        self.board[c][r] = ' X '


class Player(Board):
    def __init__(self, char_, name, points=0):
        self.char_ = ' ' + char_ + ' '
        self.name = name
        self.points = points

    def capture(self, c, r):
        super().board[c][r] = self.char_


def main():
    board = Board(10, 10)
    while True:
        col = int(input("Which column to attack? -> ")) - 1
        row = int(input("Which row to attack? -> ")) - 1

        board.capture(col, row)
        print("You've attacked field " + str(col) + ', ' + str(row) + '!')
        print("---")
        board.show()
        (n)
main()
