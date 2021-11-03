import random


def randomizer(higher):
    y = 0
    lower = 1
    x = random.randint(lower, higher)
    i = 0
    print(f"My range = ({lower}, {higher})")
    while y != x:
        y = random.randint(lower, higher)
        if y < x:
            lower = y + 1
        elif y > x:
            higher = y - 1
        i += 1
    print(f"{y} = {x} --- after {i} attempts.")
    return i


def trial(trials, higher):
    result = 0
    for j in range(int(trials)):
        result += randomizer(higher)
        print(f"({j})")

    average = result / int(trials)
    print(f"Average score: {average}")
    return average


def check_trials(trials, higher, step):
    results = []
    for i in range(10, higher, step):
        results.append(trial(trials, higher))
    j = 0
    for i in results:
        print(f"{j + 10} --> {results[int(i)]} \n")
        j += step


def main():
    while True:
        print("""
        ############################
        # 1   -> One trial         #
        # 2   -> Test trials' sets #
        # any -> exit              #
        ############################""")
        decision = input("--> ")
        if decision == '1':
            _trials = int(input("how many trials --> "))
            _higher = int(input("max number in a set --> "))
            trial(_trials, _higher)
        elif decision == '2':
            _trials = int(input("how many trials --> "))
            _higher = int(input("max number in a set --> "))
            _step = int(input("step in range --> "))
            check_trials(_trials, _higher, _step)
        else:
            break


main()
