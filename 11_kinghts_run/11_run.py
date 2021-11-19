# Write your code here

terms_set = []
definitions_set = []


class Flashcards:
    def __init__(self, front, back):
        self.front = front
        terms_set.append(front)
        self.back = back
        definitions_set.append(back)

    def check(self, guess):
        if guess == self.back:
            print("Correct!")
        elif guess in definitions_set:
            index = definitions_set.index(guess)
            print(f"Wrong. The right answer is {self.back}, but your definition is correct for {terms_set[index]}.")
        else:
            print(f"Wrong. The right answer is \"{self.back}\"")

    def remove(self):
        pass

    def load(self):
        pass

    def export(self):
        pass

    def ask(self):
        pass

    def exit(self):
        pass


def main():
    flashcards = []
    while True:
        act = input("Input the action (add, remove, import, export, ask, exit):")
        if act == "add":
            print("The card:")
            front = input()
            if front in terms_set:
                while front in terms_set:
                    print(f"The card \"{front}\" already exists. Try again:")
                    front = input()

            print("The definition of the card:")
            back = input()
            if back in definitions_set:
                while back in definitions_set:
                    print(f"The definition \"{back}\" already exists. Try again:")
                    back = input()

            flashcards.append(Flashcards(front, back))
            print(f"The pair (\"{front}\":\"{back}\") has been added.")
        elif act == "remove":
            front = input("Which card?\n")
            if front in terms_set:
                index = terms_set.index(front)
                del terms_set[index]
                del definitions_set[index]
                print("The card has been removed.")
            else:
                print(f"Can't remove \"{front}\": there is no such card.")
        elif act == "exit":
            print("Bye bye!")
            exit()


main()
