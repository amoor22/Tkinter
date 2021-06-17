from tkinter import *

root = Tk()
root.title("Calculator")
output = Entry(root, width=35, borderwidth=5)
output.grid(row=0, column=0, columnspan=3, ipady=9)
root.iconbitmap(r'tkinter_images\Tkinter Calculator Images\technological_awi_icon.ico')
one = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\one.png")
two = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\two.png")
three = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\three.png")
four = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\four.png")
five = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\five.png")
six = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\six.png")
seven = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\seven.png")
eight = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\eight.png")
nine = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\nine.png")
zero = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\zero.png")
x = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\qwer.png")
division = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\calculator.png")
clear = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\bin.png")
plus = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\plus.png")
equalsa = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\equal.png")
minus = PhotoImage(file=r"tkinter_images\Tkinter Calculator Images\minus.png")

boi = 0


def nume(num):
    global boi
    output.insert(boi, num)
    boi += 1
    print(boi)


sumi = []


def adds():
    global what
    what = "add"
    # sumi.clear()
    sumi.append(float(output.get()))
    output.delete(0, END)
    print(sumi)


def multi():
    global what
    what = "multi"
    # sumi.clear()
    sumi.append(float(output.get()))
    output.delete(0, END)
    print(sumi)


def divide():
    global what
    what = "divide"
    sumi.clear()
    sumi.append(float(output.get()))
    output.delete(0, END)
    print(sumi)


def subs():
    global what
    what = "subs"
    # sumi.clear()
    sumi.append(float(output.get()))
    output.delete(0, END)
    print(sumi)


def equals():
    global what
    if what == "add":
        sumi.append(float(output.get()))
        output.delete(0, END)
        output.insert(0, sum(sumi))
        print(sumi)
        sumi.clear()
    elif what == "multi":
        sumi.append(float(output.get()))
        output.delete(0, END)
        if len(sumi) > 1:
            first_item = sumi[0]
            itersumi = iter(sumi)
            next(itersumi)
            for x in itersumi:
                first_item *= x
            output.insert(0, first_item)
        else:
            output.insert(0, sumi[0])
        print(sumi)
        sumi.clear()
    elif what == "subs":
        sumi.append(float(output.get()))
        output.delete(0, END)
        if len(sumi) > 1:
            first_item = sumi[0]
            itersumi = iter(sumi)
            next(itersumi)
            for x in itersumi:
                first_item -= x
            output.insert(0, first_item)
        else:
            output.insert(0, sumi[0])
        print(sumi)
        sumi.clear()
    elif what == "divide":
        sumi.append(float(output.get()))
        output.delete(0, END)
        if len(sumi) > 1:
            first_item = sumi[0]
            itersumi = iter(sumi)
            next(itersumi)
            for x in itersumi:
                first_item /= x
            output.insert(0, first_item)
        else:
            output.insert(0, sumi[0])
        print(sumi)
        sumi.clear()


def clrs():
    global boi
    boi = 0
    sumi.clear()
    output.delete(0, END)


num1 = Button(root, padx=30, pady=20, text="1", command=lambda: nume(1), image=one).grid(row=3, column=0)
num2 = Button(root, padx=30, pady=20, text="2", command=lambda: nume(2), image=two).grid(row=3, column=1)
num3 = Button(root, padx=30, pady=20, text="3", command=lambda: nume(3), image=three).grid(row=3, column=2)
num4 = Button(root, padx=30, pady=20, text="4", command=lambda: nume(4), image=four).grid(row=2, column=0)
num5 = Button(root, padx=30, pady=20, text="5", command=lambda: nume(5), image=five).grid(row=2, column=1)
num6 = Button(root, padx=30, pady=20, text="6", command=lambda: nume(6), image=six).grid(row=2, column=2)
num7 = Button(root, padx=30, pady=20, text="7", command=lambda: nume(7), image=seven).grid(row=1, column=0)
num8 = Button(root, padx=30, pady=20, text="8", command=lambda: nume(8), image=eight).grid(row=1, column=1)
num9 = Button(root, padx=30, pady=20, text="9", command=lambda: nume(9), image=nine).grid(row=1, column=2)
num0 = Button(root, padx=30, pady=20, text="0", command=lambda: nume(0), image=zero).grid(row=4, column=0)
mult = Button(root, padx=30, pady=20, text="*", command=multi, image=x).grid(row=3, column=3)
div = Button(root, padx=30, pady=20, text="/", command=divide, image=division).grid(row=4, column=3)
add = Button(root, padx=30, pady=20, text="+", command=adds, image=plus).grid(row=1, column=3)
equal = Button(root, padx=30, pady=20, text="=", command=equals, image=equalsa).grid(row=4, column=1, columnspan=1)
clr = Button(root, padx=19, pady=20, text="Clear", command=clrs, image=clear).grid(row=0, column=3)
subsa = Button(root, padx=100, pady=20, text="-", command=subs, image=minus).grid(row=2, column=3)

root.mainloop()