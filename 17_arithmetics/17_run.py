import random
import os
import sys
import dialogues as dg


class Arithm:
    points = 0
    num_of_tasks = 5
    affirmatives = ["yes", "YES", "y", "Yes"]
    level = None
    levels = ["simple operations with numbers 2-9", "integral squares of 11-29"]
    mode = 0

    def guess(self, a, b, operand):
        if operand == '*':
            correct = a * b
        elif operand == '+':
            correct = a + b
        elif operand == '-':
            correct = a - b
        else:
            correct = a / b

        operand = ' ' + operand + ' '
        print(str(a) + operand + str(b))
        answer = None
        while type(answer) != int:
            try:
                answer = int(input())
            except ValueError:
                print(dg.format_err)
        if answer != correct:
            return dg.wrong
        self.points += 1
        return dg.right

    def generate_problem_low_diff(self):
        min_v = 2
        max_v = 9
        a = random.randint(min_v, max_v)
        b = random.randint(min_v, max_v)
        operand = random.choice(['+', '-', '*'])

        print(self.guess(a, b, operand))

    def guess_high_diff(self, a):
        correct = a**2
        print(a)
        answer = None
        while type(answer) != int:
            try:
                answer = int(input())
            except ValueError:
                print(dg.format_err)
        if answer != correct:
            return dg.wrong
        self.points += 1
        return dg.right

    def generate_problem_high_diff(self):
        min_v = 11
        max_v = 29
        a = random.randint(min_v, max_v)

        print(self.guess_high_diff(a))

    def get_mark(self):
        print(dg.print_final_message(self.points, self.num_of_tasks))
        d = input()
        self.mode = d in self.affirmatives

    def print_file(self):
        name = input(dg.ask_name)
        if os.path.isfile(".\\results.txt"):
            with open("results.txt", "a") as file:
                file.write(f"{name}: {self.points}/{self.num_of_tasks} in level {self.level} ({self.levels[self.level - 1]})\n")
        else:
            with open("results.txt", "w") as file:
                file.write(f"{name}: {self.points}/{self.num_of_tasks} in level {self.level} ({self.levels[self.level - 1]})\n")
        print(dg.saved_results)

    def print_interface(self):
        print(dg.choose_level)
        print("1 - " + self.levels[0])
        print("2 - " + self.levels[1])
        try:
            self.level = int(input())
        except ValueError:
            print(dg.bye)

    def __init__(self):
        self.print_interface()
        if self.level not in [1, 2]:
            sys.exit()
        if self.level == 1:
            for _ in range(self.num_of_tasks):
                self.generate_problem_low_diff()
        elif self.level == 2:
            for _ in range(self.num_of_tasks):
                self.generate_problem_high_diff()
        self.get_mark()
        if self.mode:
            self.print_file()


Arithm()
