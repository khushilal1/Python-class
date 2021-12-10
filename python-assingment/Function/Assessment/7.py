# 7. Program to display calendar using calendar module
import calendar

print("INTERNATIONAL  CALENDAR  AS YOUR CHOICE")
year=int(input("Enter year:\n"))
month=int(input("Enter month:\n"))
a=calendar.month(year,month)
b=calendar.calendar(year)
print(a)
print(b)



