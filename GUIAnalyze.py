import os
from tkinter import Tk
from tkinter import Button
from tkinter import ANCHOR
from tkinter import CENTER
from tkinter import PanedWindow
from tkinter import Label
from tkinter.filedialog import askopenfilename


def chooseFile():
    filename = askopenfilename()
    os.system("python3 analyze.py " + filename)
    quit()


"""
root = Tk()
root.title('Choose File')
root.config(height=200, width=400)

# Panel
panel = PanedWindow()
panel.pack(expand=0)

# Label
label = Label(panel, text='Seleziona il file da analizzare')
label.grid(row=0, column=0)
label.pack()

# Button
mybutton = Button(panel, text="Scegli il file", command=chooseFile, fg="blue")
mybutton.grid(row=1, column=0)
mybutton.pack()

# Posiziono il panel al centro della root e gli metto gli elementi al centro
panel.place(relx=0.5, rely=0.5, anchor=CENTER)

# Position
w = label.winfo_reqwidth()
h = label.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (root.winfo_reqwidth(),root.winfo_reqheight(), x-400, y- 200))

root.mainloop()
"""

chooseFile()

if __name__ == '__main__':
    chooseFile()
