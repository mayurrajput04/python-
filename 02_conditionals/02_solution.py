age = int(input("Enter age : "))
day = input("Enter day : ")

price = 12 if age >= 18 else 8

if day == "Wednesday" or day =="wednesday" :
    price = 10 if age >= 18 else 6

print("$",price)
