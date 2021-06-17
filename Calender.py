import calendar
import datetime
from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('175x180')

def get_cal():
    display.delete(1.0,END)
    month = int(months_list[month_button.get()])
    year = int(year_button.get())
    display.insert(INSERT, calendar.month(year, month))


months_list = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7,
               'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
#reversed dictionary
months_list_rev = dict(map(reversed, months_list.items()))

years_list = []
yar = 1900
for x in range(151):
    years_list.append(yar)
    yar += 1
years_list.reverse()
default_month = StringVar(root)
default_month.set(months_list_rev[datetime.date.today().month])

default_year = StringVar(root)
default_year.set(datetime.date.today().year)

display = Text(root,foreground='red',background='black',width=21)
display.grid(row=2,column=0,columnspan=2)

month_button = ttk.Combobox(root,textvariable=default_month,values=[*months_list],width=10)
month_button.grid(row=0,column=0)

year_button = ttk.Combobox(root,textvariable=default_year,values=[*years_list],width=10)
year_button.grid(row=0,column=1)

submit_button = Button(root,padx=50,pady=10,command=get_cal,text='Get Calender')
submit_button.grid(row=1,column=0,columnspan=2)
#print(calendar.month(2020,1))
root.mainloop()