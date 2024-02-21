pet = "Dog"
pet_age = int(input("Enter age of your pet : "))

if pet == "Dog" :
    if pet_age < 2 :
        food = "Puppy food "
    else :
        food = "Senior Pet food "
elif pet == "Cat":
    if pet_age > 5 :
        food = "Senior Pet food"
    else:
        food = "Baby pet food"
else :
    print("Choose correct pet type")

print("You should feed your pet" ,food)