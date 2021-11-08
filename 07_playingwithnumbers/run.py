import lib.funcs
import os
# this program lets the user join their expenses into a txt file, then the algorithm adds data from every line to print
# a sum of every value in the file


class Expenses:
    def __init__(self, expense):
        self.expense = "data/" + expense + ".txt"

        # if the file doesn't exist, create it
        try:
            f = open(self.expense, "r")
        except FileNotFoundError:
            print("Hmmm, looks like this file doesn't exist. Do you want to create a new file?")
            d = input("[Y]es --> ")
            if d.upper() == 'Y':
                print("I'm creating a file called " + self.expense)
                file = open(self.expense, "w")
                file.write("")
                file.close()
            else:
                self.expense = None

    def clear_file(self):
        file = open(self.expense, "w")
        file.write("")
        file.close()

    def add_value(self, value):
        file = open(self.expense, "a")
        file.write(value + '\n')
        file.close()

    def sum_values(self):
        file = open(self.expense, "r")
        values = file.readlines()
        sum = 0
        for value in values:
            sum += int(value)

        return sum

    def del_file(self):
        os.remove(self.expense)


def main():
    exp = None

    while exp is None or exp.expense is None:
        lib.funcs.showfiles("data/*.txt")
        print("\n*****\n")
        print("Type the expense file you want to access")
        choice = input(" --> ")
        exp = Expenses(choice)
        try:
            print("You've chosen " + exp.expense + " as your file.")
        except TypeError:
            print("Well, I'll consider this as a typo, try again then!")

    while True:
        print(""" 1 --> clear the file
                      2 --> add new values
                      3 --> sum the values
                      4 --> delete the file
                      5 --> exit""")
        d = input(" -> ")
        if d == '1':
            exp.clear_file()
        elif d == '2':
            while True:
                v = input("Type your value: ")
                exp.add_value(v)
                if input("Continue? [y/Y]: ") not in ['y', 'Y']:
                    break
        elif d == '3':
            print(exp.sum_values())
        elif d == '4':
            confirm = input("Do you really want to delete this file? Type " + exp.expense + " to confirm: ")
            if confirm == exp.expense:
                exp.del_file()
                print("File has been deleted!")
                break
        elif d == '5':
            break
        else:
            print("Wrong input!")


main()
