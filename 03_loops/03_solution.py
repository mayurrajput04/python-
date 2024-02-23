num = int(input("Enter the Number : "))
print(f"Mutiplication table of {num}")

for count in range(1 ,11):
    if count == 5:
        continue
    print(f"{num} x {count} = {num*count}")
    