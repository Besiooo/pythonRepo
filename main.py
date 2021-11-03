import glob


def showfiles():
    myfiles = glob.glob("*_*")
    for item in myfiles:
        print(f"{item}")

def print_hi(name):
    print(f"Hi, I'm {name} and here are your files: ")


if __name__ == '__main__':
    print_hi('PyCharm')
    showfiles()
