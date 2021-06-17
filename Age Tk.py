from tkinter import *
from tkinter import ttk
import datetime
from time import sleep
from math import floor
from dateutil.relativedelta import relativedelta

# import ttk
root = Tk()
root.geometry("950x500")
root.title('Age Calculator')
root.iconbitmap(r'tkinter_images\Tkinter Calculator Images\technological_awi_icon.ico')

check = PhotoImage(file=r"tkinter_images\correct.png")

minutes_list = []
for x in range(0, 60):
    if x < 10:
        minutes_list.append("0"+str(x))
    else:
        minutes_list.append(x)
hours_list = []
for x in range(1, 13):
    hours_list.append(x)

days_list = []
months_list = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7,
               'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

years_list = []
yar = 1900

months_list_rev = dict(map(reversed, months_list.items()))
for x in range(151):
    years_list.append(yar)
    yar += 1

years_list.reverse()
for x in range(1, 32):
    days_list.append(x)
# default day
default_day = StringVar(root)
default_day.set(days_list[0])
# default month
default_month = StringVar(root)
default_month.set(months_list_rev[1])
# default year 46
default_year = StringVar(root)
default_year.set(years_list[46])

default_hour = StringVar(root)
default_hour.set(hours_list[0])

default_minute = StringVar(root)
default_minute.set(minutes_list[0])

days = ttk.Combobox(root, textvariable=default_day, values=[*days_list], width=5)
days.grid(row=1, column=0)

months = ttk.Combobox(root, textvariable=default_month, values=[*months_list], width=9)
months.grid(row=1, column=1)

years = ttk.Combobox(root, textvariable=default_year, values=[*years_list], width=9)
years.grid(row=1, column=2)

hours = ttk.Combobox(root, textvariable=default_hour, values=[*hours_list], width=9)
hours.grid(row=1, column=3)

minutes = ttk.Combobox(root, textvariable=default_minute, values=[*minutes_list], width=9)
minutes.grid(row=1, column=4)


def am():
    global liv_hour
    liv_hour = hours.get()

def pm():
    global liv_hour
    liv_hour = int(hours.get()) + 12
    return liv_hour

v = IntVar()
Radiobutton(root, text='AM', variable=v, value=1, command=am).grid(row=1, column=6)
Radiobutton(root, text='PM', variable=v, value=2, command=pm).grid(row=1, column=7)


def find_things():
    global liv_hour
    v.set(0)
    bday_dt = datetime.datetime(int(years.get()), int(months_list[months.get()]), int(days.get()), int(liv_hour),
                                int(minutes.get()))
    dt = datetime.datetime.today()
    d = datetime.date.today()
    days_on_e = (dt - bday_dt).days
    year_old = floor((dt - bday_dt).days / 365) #useless
    year_old2 = relativedelta(dt,bday_dt).years
    mon_old = abs(dt.month - bday_dt.month) #useless
    mon_old2 = relativedelta(dt,bday_dt).months
    day_old = abs(dt.day - bday_dt.day) #useless
    day_old2 = relativedelta(dt,bday_dt).days
    hour_old = dt.hour - bday_dt.hour   #useless
    hour_old2 = relativedelta(dt,bday_dt).hours
    minute_old = dt.minute - bday_dt.minute #useless
    minute_old2 = relativedelta(dt,bday_dt).minutes
    day_o_week = bday_dt.weekday()
    weekday = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    name_weekday = weekday[day_o_week]
    if minute_old < 0:  #useless
        hour_old -= 1
        minute_old = 60 - abs(minute_old)
    if int(hour_old) < 0:   #useless
        day_old -= 1
        hour_old = 24 - abs(hour_old)

    new_birthday = datetime.datetime(dt.year, bday_dt.month, bday_dt.day, int(liv_hour), int(minutes.get()))
    if relativedelta(new_birthday,dt).months < 0 or relativedelta(new_birthday, dt).days < 0 or relativedelta(new_birthday, dt).hours < 0 or relativedelta(new_birthday, dt).minutes < 0:
        new_birthday = datetime.datetime(dt.year + 1, bday_dt.month, bday_dt.day, int(liv_hour), int(minutes.get()))
    till_day = new_birthday - dt

    till_month_act = relativedelta(new_birthday,dt).months
    till_day_act = relativedelta(new_birthday, dt).days
    till_hour_act = relativedelta(new_birthday, dt).hours
    till_minute_act = relativedelta(new_birthday, dt).minutes
    label = Label(root,
                  text="You are {} years {} months {} days {} hours {} minutes old.\nYou have lived {} days.\nYou were born on {}, {}:{}, {}/{}/{}\nYour next birthday will be in {} month(s) {} day(s) {} hour(s) and {} minute(s)".format(
                      year_old2, mon_old2, day_old2, hour_old2, minute_old2, days_on_e, name_weekday, hours.get(),
                      minutes.get(), days.get(), months.get(), years.get(),till_month_act,till_day_act,till_hour_act,till_minute_act), font="Time 15")
    label.grid(row=2, column=1, columnspan=3)
    return bday_dt


submit = Button(root, command=find_things, padx=100, pady=75, image=check)
submit.grid(row=3, column=2)
# print(find_things())

root.mainloop()
