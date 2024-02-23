string = input("Enter your string : ")

for char in string:
    if string.count(char) == 1:
        print(f"char is : {char}")
        break