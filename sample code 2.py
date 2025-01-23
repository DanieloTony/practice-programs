# here we write a program for leap year:

year = int(input("Enter the year:"))

if year % 4 == 0 or year % 400 == 0:
    print(year, " is a leap year")
else:
    print(year, "not a leap year") 