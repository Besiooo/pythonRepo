from classes.family import Library


def ui():
    my_library = Library()

    print("-----> Welcome to " + my_library.Name + " <-----")
    while True:
        print("""Choose your action:
                        1 - add a book
                        2 - show the books
                        3 - remove a book
                        0 - exit
                        """)
        x = input("--> ")

        if x == '1':
            my_library.addBook()
            continue
        if x == '2':
            my_library.showBooks()
            continue
        if x == '3':
            my_library.deleteBook()
            continue
        if x not in {1, 2, 3} or x == 0:
            break


def main():
    ui()


main()
