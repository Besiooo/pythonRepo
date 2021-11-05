from player import HumanPlayer, AIPlayer
from game import TicTacToe


def play(game, x_player, o_player, print_game=True):
    # play returns the winner, or None when tied
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter

    while game.empty_squares():
        # get the move from an appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" -----> {square}")
                game.print_board()
                print('')

        if game.current_leader:
            if print_game:
                print(letter + " wins!")
            return letter

        # we need to swap the letter after making a move
        letter = 'O' if letter == 'X' else 'X'

        if print_game:
            print("It's a tie! ")


if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = HumanPlayer('O')

    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
