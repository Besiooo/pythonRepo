from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)  # xpos, ypos, width, height
        self.setWindowTitle("Test Application")  # sets window title
        self.init_ui()

    def init_ui(self):  # all the stuff we want in a window
        self.label = QtWidgets.QLabel(self)  # sets a new label that is a child of window (so it's self)
        self.label.setText("Jajeczko")  # sets text
        self.label.move(100, 50)  # sets position of label relative to parents origin @0,0 (xpos, ypos)

        self.b1 = QtWidgets.QPushButton(self)  # sets a button that is a child of window (so it's self)
        self.b1.setText("Guziorek")  # sets text visible on the button
        self.b1.move(98, 260)  # moves the button on canvas
        self.b1.clicked.connect(self.clicked)  # links previously defined function to this button

    def clicked(self):
        self.label.setText("You pressed it!")
        self.update()

    def update(self):  # adjust size so the text will be visible no matter how long
        self.label.adjustSize()


def clicked():
    print("Clicked")


