# THIS WILL WORK, I PROMISE! :D

import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()  # holds the whole structure of my application
apps = []

if os.path.isfile("save.txt"):  # memory module: if there is a save file, then read from it
    with open("save.txt", 'r') as f:
        temp_apps = f.read()
        temp_apps = temp_apps.split(',')
        apps = [x for x in temp_apps if x.strip()] # removes empty entries


def add_apps():
    for labels in frame.winfo_children():
        labels.destroy()
    # ^ for every item that sits in a parent-label, delete that item
    # in this case this prevents from printing 1-1-2-1-2-3-1-2-3-4 instead of 1-2-3-4 problem

    file_name = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(file_name)
    for app_ in apps:
        label_ = tk.Label(frame, text=app_, fg="#65655E", bg="#CEBACF")
        label_.pack()
    # prints out dirs of selected files on the frame


def run_apps():
    for app_ in apps:
        os.startfile(app_)


canvas = tk.Canvas(root, height=300, width=450, bg="#7D80DA")  # builds the area which my app works on
canvas.pack()  # attaches canvas to the root, so it makes it visible on gui

frame = tk.Frame(root, bg="#CEBACF")  # builds a plain rectangle (frame) on gui
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.06)
# ^^ places the frame on gui - it's size is relative of canvas' resolutions (relwidth, relheight)
# relx, rely -> puts margins that equals 0.1 of canvas reso from each side:
#   <    0.1    >
#  0.1   0.8   0.1   ---> the frame is centered now as all sides sums to 1.0
#   <    0.1    >

# DECLARING BUTTONS

open_file = tk.Button(root, text="Open file", padx=5, pady=5, fg="#65655E", bg="#C6AFB1", command=add_apps)
# open_file.place(relwidth=0.2, relheight=0.05, relx=0.4, rely=0.925)
open_file.pack()

run_apps = tk.Button(root, text="Run apps", padx=5, pady=5, fg="#65655E", bg="#C6AFB1", command=run_apps)
run_apps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()
# ^ shows files that have been read from memory

root.resizable(False, False)  # locks resize opt
root.mainloop()  # runs my gui

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
