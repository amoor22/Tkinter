from Tkinter import *
import datetime

dt = datetime.datetime.today()
print("The date-time (today):", dt)
bday_dt = datetime.datetime(2004, 7, 3, 23, 0, 0)
print((dt-bday_dt).days)
print((dt-bday_dt).days/365)
print(abs(dt.month - bday_dt.month))
print(abs(dt.day - bday_dt.day))
print(abs(dt.hour - bday_dt.hour))
print(abs(dt.minute - bday_dt.minute))
b = datetime.date.today()
bday = datetime.date(2004, 7, 3)
print("Day born on (saturday):", bday.weekday())  # saturday
days_lived = b - bday

print(float(days_lived.days) / 365)

a = datetime.timedelta(days=365 * 15)
print(a.total_seconds() / (86400))

d = datetime.timedelta(weeks=2)
print(d.days, d.seconds, d.microseconds)
