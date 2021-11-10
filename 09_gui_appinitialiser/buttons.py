from app import frame
import tkinter as tk
from tkinter import filedialog, Text
import os

apps = []


def add_apps():
    file_name = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(file_name)
    for app in apps:
        label = tk.Label(frame, text=app, fg="#65655E")
    # opens a window that asks for a file -> you can select between executables only, and all files
    # then stores the exact location of selected file in this variable above

