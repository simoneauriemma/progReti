import os
from tkinter.filedialog import askopenfilename
import tkinter
import tkinter.filedialog


def choose_file():
    root = tkinter.Tk()
    files = tkinter.filedialog.askopenfilenames(parent=root, title='Choose a file')

    for file in root.tk.splitlist(files):
        os.system("python3 analyze.py " + file)
    quit()


choose_file()


if __name__ == '__main__':
    choose_file()
