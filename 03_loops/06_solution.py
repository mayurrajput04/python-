num = int(input("Enter the Number : "))
factorial = 1

while num > 0:
    factorial = factorial*num
    num = num - 1
print(f"Factorial is : {factorial}") 