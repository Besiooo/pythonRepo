def initialise(directory, content):
    file = open(directory, "w")
    file.write(content)
    file.close()


def read_file(directory):
    file = open(directory, "r")
    print(file.read())
    file.close()


def main():
    base = """0 - Zero
1 - One
2 - Two
3 - Three
4 - Four
5 - Five
6 - Six
7 - Seven
8 - Eight
9 - Nine
10 - Ten"""
    initialise("numbers.txt", base)

    numbers_file = open("numbers.txt", "r")
    print("Readable? " + str(numbers_file.readable()))
    print(numbers_file.read())          # switches the virtual cursor to the end
    numbers_file.close()
    print("---")

    numbers_file = open("numbers.txt", "r")
    print(numbers_file.readline())      # switches the virtual cursor to the next line
    print(numbers_file.readline())
    print(numbers_file.readline())
    print(numbers_file.readline())
    numbers_file.close()

    numbers_file = open("numbers.txt", "r")
    print("---")
    # print(numbers_file.readlines())     # makes a list of lines in the text
    for number in numbers_file.readlines():
        print(number)
    numbers_file.close()

    # APPENDING TO A FILE --> adding to an end of a file
    numbers_file = open("numbers.txt", "a")
    numbers_file.write("\n20 - Twenty (added using code)")
    numbers_file.close()
    read_file("numbers.txt")

    # OVERRIDE A FILE --> look line 1

    # CREATE A NEW FILE
    i = 0
    while True:
        d = input("Add a file? [Y] --> ")
        if d == 'Y':
            file_name = "coded" + str(i) + ".txt"
            initialise(file_name, "test!")
            i += 1
        else:
            break


main()
