import random

def is_true(user_choice, comp_choice):
    if(user_choice == 'R' and comp_choice == 'S') or (user_choice == 'S' and comp_choice == 'P') or \
      (user_choice == 'P' and comp_choice == 'R'):
        return True


def algorithms():
    user = input("[R]ock, [P]aper, [S]cissors ---> ").upper()
    # user = user.upper()
    comp = random.choice(['R', 'P', 'S'])

    if user == comp:
        return 0

    if is_true(user, comp):
        return 1

    return 2


def play(rounds):
    user_score = 0
    comp_score = 0
    for one_round in range(0, rounds):
        result = algorithms()
        if result == 0:
            user_score = user_score + 1
            comp_score = comp_score + 1
            print(f"It's a tie! \n YOU {user_score} - {comp_score} COMP")
        elif result == 1:
            user_score = user_score + 1
            print(f"You won! \n YOU {user_score} - {comp_score} COMP")
        elif result == 2:
            comp_score = comp_score + 1
            print(f"You lost! \n YOU {user_score} - {comp_score} COMP")
        else:
            print(f"FATAL ERROR! GAME ENDED \n YOU {user_score} - {comp_score} COMP")


def main():
    rounds = int(input("How many rounds?"))
    play(rounds)


main()