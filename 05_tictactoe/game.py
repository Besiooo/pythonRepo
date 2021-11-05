from player import HumanPlayer, AIPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # using a list of 9 to make a 3x3 board
        self.current_leader = None  # stores the current leader of the game

    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:  # defines row length of 3 and splits them
            print('| ' + ' |'.join(row) + ' |')

    @staticmethod  # static because it stays the same no matter what; we don't pass 'self' in it
    def print_board_nums():
        # 0  1  2
        # 3  4  5
        # 6  7  8
        num_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        # ^ this makes an array of 3 subarrays (because range(3)), each one of them stores 3 indeces range(j*3, (j+1)*3)
        for row in num_board:
            print('| ' + ' | '.join(row) + ' |')

        # what are the available moves after you make a move --> we cannot put a mark on previously marked spot!
        # function below returns an array of indeces that are available

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

        #   moves = []      # stores tuples [index -> mark]; [(0, 'X'), (1, 'X'), (2, 'O')]
        #   for(i, spot) in enumerate(self.board):
        #       if spot == ' ':         # if a spot is blank
        #           moves.append(i)     # add it to list of moves
        #   return moves
        #   ENUMERATE --> lets me print an index and a value from an array
        # ^ this can be represented just in one line:

    def empty_squares(self):
        return ' ' in self.board  # True / False (are any free spaces in the board?

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if the move is valid: make the move, then return false
        # if the move is invalid: return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner has to have three of its marks aligned vertically, horizontally, or diagonally
        # CHECKING ROWS
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):  # if all spots in a row has the same letter, we got a winner
            return True

        # CHECKING COLUMNS
        col_ind = square % 3
        col = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        # CHECKING DIAGONALS
        # 0     2
        #    4   ----> ONLY EVEN NUMBERS
        # 6     8
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False
