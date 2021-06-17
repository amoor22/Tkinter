from tkinter import *

root = Tk()
def exot():
    labol = Label(root, text="I clicked a button")
    labol.pack()
butt = Button(root, text="Deez Nuts", command=exot,fg="yellow",bg="purple")
butt.pack()
root.mainloop()