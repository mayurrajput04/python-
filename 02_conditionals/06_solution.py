distance = int(input("Enter distance : "))


if distance < 3 :
    mode = "Walk"
elif distance < 16 :
    mode = "Bike"
elif distance > 15 :
    mode = "Car"
else:
    print("Mode not Available")

print("Transport : ",mode)    