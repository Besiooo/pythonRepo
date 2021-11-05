import lib.words    # lib.words.words --> array of words // lib.words.vowels ---> array of vowels (lowercase)
import random


# scratcher --> swaps all vowels in a word to X's
def scratcher(word, uppercase=False):
    result = ""
    for letter in word:
        if letter in lib.words.vowels:
            result = result + 'x'
        else:
            result = result + letter

    return result.upper() if uppercase else result


# to_column --> prints a word in a column
def to_column(word):
    for letter in word:
        print(letter)


# commoner --> takes two words of different sizes; if the longer one has common letters with the shorter one, uppercase
# these; letters that are beyonf the smaller's range changes into $
def commoner(word_a):
    word_b = ""
    while len(word_b) < len(word_a):
        word_b = random.choice(lib.words.words)

    result = ""
    for (i, letter) in enumerate(word_b):
        if i >= len(word_a):
            result += '$'
            continue
        if letter in word_a:
            result += letter.upper()
        else:
            result 4+= letter

    print(word_a + ' -><- ' + word_b + " = " + result)


def main():
    the_word = random.choice(lib.words.words)
    print(the_word)
    print(scratcher(the_word))
    to_column(the_word)
    commoner(the_word)


main()