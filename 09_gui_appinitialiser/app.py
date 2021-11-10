import tkinter as tk
from tkinter import filedialog
import os
import sys


class MyProgram:
    def __init__(self, apps_):
        self.apps_ = apps_
        self.memory_module()
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=300, width=450, bg="#7D80DA")
        self.frame = tk.Frame(self.root, bg="#CEBACF")
        self.open_file = tk.Button(self.root, text="Open file", padx=5,
                                   pady=5, fg="#65655E", bg="#C6AFB1", command=self.add_apps)
        self.run_apps = tk.Button(self.root, text="Run apps", padx=5,
                                  pady=5, fg="#65655E", bg="#C6AFB1", command=self.run_apps)
        self.del_apps = tk.Button(self.root, text="Clear apps", padx=5,
                                  pady=5, fg="#65655E", bg="#C6AFB1", command=self.clear_memory)
        self.init_ui()

    def init_ui(self):
        self.canvas.pack()
        self.frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.06)
        self.open_file.pack()
        self.open_file.place(x=120, y=304)
        self.run_apps.pack()
        self.del_apps.pack()
        self.del_apps.place(x=268, y=304)
        for app in self.apps_:
            label = tk.Label(self.frame, text=app)
            label.pack()
        self.root.resizable(False, False)
        self.root.mainloop()
        self.memory_write()

    def add_apps(self):
        for labels in self.frame.winfo_children():
            labels.destroy()

        file_name = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("executables", "*.exe"), ("all files", "*.*")))
        self.apps_.append(file_name)
        for app_ in self.apps_:
            label_ = tk.Label(self.frame, text=app_, fg="#65655E", bg="#CEBACF")
            label_.pack()

    def run_apps(self):
        for app_ in self.apps_:
            os.startfile(app_)

    def memory_module(self):
        if os.path.isfile("save.ptd"):
            with open("save.ptd", 'r') as f:
                temp_apps = f.read()
                temp_apps = temp_apps.split('\n')
                self.apps_ = [x for x in temp_apps if x.strip()]

    def memory_write(self):
        with open('save.ptd', 'w') as f:
            for app in self.apps_:
                f.write(app + '\n')

    def clear_memory(self):
        self.apps_ = ''
        self.memory_write()
        python = sys.executable
        os.execl(python, python, *sys.argv)


MyProgram(apps_=[])
