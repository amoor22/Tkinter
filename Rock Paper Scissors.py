from tkinter import *
from random import randint
root = Tk()
root.title("RPS")
rand = randint(1,3)
rock_img = PhotoImage(file=r"tkinter_images\RPS Tkinter\stone.png")
paper_img = PhotoImage(file=r"tkinter_images\RPS Tkinter\paper-plane.png")
scissors_img = PhotoImage(file=r"tkinter_images\RPS Tkinter\cut.png")
play_img = PhotoImage(file=r"tkinter_images\RPS Tkinter\play.png")
retry_img = PhotoImage(file=r"tkinter_images\RPS Tkinter\replay.png")
def rock():
    global choose
    choose = 1
def paper():
    global choose
    choose = 2
def scissors():
    global choose
    choose = 3
def retry():
    global rand
    global c_choose
    rand = randint(1, 3)

    rock_button = Button(root, text="rock", padx=20, pady=20, command=rock, image=rock_img)
    paper_button = Button(root, text="paper", padx=20, pady=20, command=paper, image=paper_img)
    scissors_button = Button(root, text="scissors", padx=20, pady=20, command=scissors, image=scissors_img)

    rock_button.grid(row=1, column=0)
    paper_button.grid(row=1, column=1)
    scissors_button.grid(row=1, column=2)

    c_choose = Label(root, width=9, height=5)
    label = Label(root, width=10, height=3)

    c_choose.grid(row=0, column=0, columnspan=1)
    label.grid(row=0, column=1, columnspan=2)

def start():
    global choose
    if choose == 1:
        paper_button = Button(root, text="paper", padx=20, pady=20, command=paper, image=paper_img,state=DISABLED)
        scissors_button = Button(root, text="scissors", padx=20, pady=20, command=scissors, image=scissors_img,state=DISABLED)

        paper_button.grid(row=1, column=1)
        scissors_button.grid(row=1, column=2)
    elif choose == 2:
        rock_button = Button(root, text="rock", padx=20, pady=20, command=rock, image=rock_img,state=DISABLED)
        scissors_button = Button(root, text="scissors", padx=20, pady=20, command=scissors, image=scissors_img,state=DISABLED)

        rock_button.grid(row=1, column=0)
        scissors_button.grid(row=1, column=2)
    elif choose == 3:
        rock_button = Button(root, text="rock", padx=20, pady=20, command=rock, image=rock_img,state=DISABLED)
        paper_button = Button(root, text="paper", padx=20, pady=20, command=paper, image=paper_img,state=DISABLED)

        rock_button.grid(row=1, column=0)
        paper_button.grid(row=1, column=1)

    if rand == 1:
        c_choose = Label(root, width=64, height=64, image=rock_img)
        c_choose.grid(row=0, column=0, columnspan=1)
    elif rand == 2:
        c_choose = Label(root, width=64, height=64, image=paper_img)
        c_choose.grid(row=0, column=0, columnspan=1)
    elif rand == 3:
        c_choose = Label(root, width=64, height=64, image=scissors_img)
        c_choose.grid(row=0, column=0, columnspan=1)
    if rand == choose:
        label = Label(root, width=10, height=3,text="It's a draw")
        label.grid(row=0, column=1, columnspan=2)
        print(rand,choose)
    elif choose == 1 and rand == 2:
        label = Label(root, width=10, height=3, text="You Lose")
        label.grid(row=0, column=1, columnspan=2)
        print(choose, rand)
    elif choose == 1 and rand == 3:
        label = Label(root, width=10, height=3, text="You Win")
        label.grid(row=0, column=1, columnspan=2)
        print(choose, rand)
    elif choose == 2 and rand == 1:
        label = Label(root, width=10, height=3, text="You Win")
        label.grid(row=0, column=1, columnspan=2)
        print(choose, rand)
    elif choose == 2 and rand == 3:
        label = Label(root, width=10, height=3, text="You Lose")
        label.grid(row=0, column=1, columnspan=2)
        print(choose, rand)
    elif choose == 3 and rand == 1:
        label = Label(root, width=10, height=3, text="You Lose")
        label.grid(row=0, column=1, columnspan=2)
        print(choose, rand)
    elif choose == 3 and rand == 2:
        label = Label(root, width=10, height=3, text="You Win")
        label.grid(row=0, column=1, columnspan=2)
        print(choose, rand)
c_choose = Label(root, width=9, height=5)
label = Label(root,width=10,height=3)

rock_button = Button(root,text="rock",padx=20,pady=20,command=rock,image=rock_img)
paper_button = Button(root,text="paper",padx=20,pady=20,command=paper,image=paper_img)
scissors_button = Button(root,text="scissors",padx=20,pady=20,command=scissors,image=scissors_img)
start_button = Button(root, text="start", padx=20, pady=20, command = start,image=play_img)
retry_button = Button(root, text="retry", padx=20, pady=20, command = retry,image=retry_img)

c_choose.grid(row=0,column=0,columnspan=1)
label.grid(row=0,column=1,columnspan=2)

rock_button.grid(row=1,column=0)
paper_button.grid(row=1,column=1)
scissors_button.grid(row=1,column=2)
retry_button.grid(row=2,column=2)

start_button.grid(row=2,column=1,columnspan=1)
root.mainloop()