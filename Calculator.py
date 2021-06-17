from tkinter import *

root = Tk()
root.title("Calculator")
ass = Entry(root,width=35,borderwidth=5)
ass.grid(row=0,column=0,columnspan=3)
#,justify=RIGHT
boi = 0

def nume(num):
    global boi
    ass.insert(boi,num)
    boi += 1
def nume1():
    global boi
    ass.insert(boi,"1")
    boi += 1
def nume2():
    global boi
    ass.insert(boi,"2")
    boi += 1
def nume3():
    global boi
    ass.insert(boi,"3")
    boi += 1
def nume4():
    global boi
    ass.insert(boi,"4")
    boi += 1
def nume5():
    global boi
    ass.insert(boi,"5")
    boi += 1
def nume6():
    global boi
    ass.insert(boi,"6")
    boi += 1
def nume7():
    global boi
    ass.insert(boi,"7")
    boi += 1
def nume8():
    global boi
    ass.insert(boi,"8")
    boi += 1
def nume9():
    global boi
    ass.insert(boi,"9")
    boi += 1
def nume0():
    global boi
    ass.insert(boi,"0")
    boi += 1
sumi = []
def adds():
    sumi.clear()
    sumi.append(int(ass.get()))
    ass.delete(0,999)
    print(sumi)
def equals():
    sumi.append(int(ass.get()))
    ass.delete(0, 999)
    ass.insert(0,sum(sumi))
    print(sumi)
    sumi.clear()
def clrs():
    global boi
    boi = 0
    sumi.clear()
    ass.delete(0, 999)
num1 = Button(root,padx=30,pady=20,text="1",command=nume1).grid(row=3,column=0)
num2 = Button(root,padx=30,pady=20,text="2",command=nume2).grid(row=3,column=1)
num3 = Button(root,padx=30,pady=20,text="3",command=nume3).grid(row=3,column=2)
num4 = Button(root,padx=30,pady=20,text="4",command=nume4).grid(row=2,column=0)
num5 = Button(root,padx=30,pady=20,text="5",command=nume5).grid(row=2,column=1)
num6 = Button(root,padx=30,pady=20,text="6",command=nume6).grid(row=2,column=2)
num7 = Button(root,padx=30,pady=20,text="7",command=nume7).grid(row=1,column=0)
num8 = Button(root,padx=30,pady=20,text="8",command=nume8).grid(row=1,column=1)
num9 = Button(root,padx=30,pady=20,text="9",command=nume9).grid(row=1,column=2)
num0 = Button(root,padx=30,pady=20,text="0",command=nume0).grid(row=5,column=0)
add = Button(root,padx=30,pady=20,text="+",command=adds).grid(row=6,column=1)
equal = Button(root,padx=30,pady=20,text="=",command=equals).grid(row=6,column=2)
clr = Button(root,padx=19,pady=20,text="Clear",command=clrs).grid(row=6,column=0)
root.mainloop()