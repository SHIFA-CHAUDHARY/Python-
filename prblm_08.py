Password = input("Enter Your password")

if len(Password) < 6:
    print("weak password")
    
elif len(Password) <= 10 :
    print("Medium Password")
    
else:
    print("Strong Password")
    