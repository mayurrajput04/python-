Password = "pass@123"

if len(Password) < 6 :
    pwd = "Weak"
elif len(Password) <= 10:
    pwd = "Normal"
else:
    pwd = "Strong"

print("Your Password is" ,pwd)

