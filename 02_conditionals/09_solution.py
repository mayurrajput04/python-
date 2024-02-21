year = int(input("ENter the year :"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
    print("Given year is leap year ")
else :
    print("Given year is not a leap year ")   