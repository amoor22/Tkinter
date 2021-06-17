from tkinter import *

root = Tk()

inp = Entry(root, width=60, borderwidth=5)
inp.pack()
inp.get()
inp.insert(0,"Enter your name")
def exot():
    labol = Label(root, text="Hello! "+ inp.get())
    labol.pack()
butt = Button(root, text="Deez Nuts", command=exot,fg="yellow",bg="purple", padx=30,pady=40)
butt.pack()
root.mainloop()