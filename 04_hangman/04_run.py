import random
from words import words
import string


#  array of words from a file called words.py that is in the same directory as this file


def ai_choose_word(words_set):
    word = random.choice(words_set)  # take a word from the set of english words
    while '-' in word or ' ' in word:     # if a word is invalid (includes spaces or dashes) take a different word until you get a right one
        word = random.choice(words_set)
    return word.upper()           # return a valid word


def hangman():
    word = ai_choose_word(words)    # take a goal-word into the game
    word_letters = set(word)        # break the word into a set of letters
    alphabet = set(string.ascii_uppercase)  # take a set with all uppercase letters in the english alphabet
    used_letters = set()            # make a set of all the letter the user tried

    # algorithm:
    # user tries a letter (1):
    # when they guess right (1a) --> subtract the letter from the set of the word's letters (A) and and this letter to the set of used letters (B)
    # when they guess wrong (1b) --> add this letter to the set of used letters (B)
    # game ends when the set of the word's letters is empty (C) (all of the letters are guessed, so they're subtracted)
    while len(word_letters) > 0:    # (C)
        print("You have used: ", ' '.join(used_letters))    # .join(set) --> prints all elements of a set seperated by a char

        # the board: makes a set of the word's letters --> if they're guessed (letter in used words) show them
        # if they're not guessed, print '-' instead
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Board -->", ' '.join(word_list))

        user_input = input("Give a letter: ").upper()
        if user_input in alphabet - used_letters:   # in alphabet, not used --> player can check this letter
            used_letters.add(user_input)         # mark the letter as used
            if user_input in word_letters:          # in the actuall word --> player guessed one letter
                word_letters.remove(user_input)     # remove the letter from the set of letters the player has to guess

        elif user_input in used_letters:            # in used_letters --> player has already checked this letter
            print("You have used this letter before!")

        else:                                       # not in alphabet --> invalid input
            print("Invalid input!")


hangman()
