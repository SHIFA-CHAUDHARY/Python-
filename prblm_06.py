Distance = int(input("Enter Your Distance"))

if Distance < 3 :
    print("Prefer Walking")
    
elif Distance < 15 :
    print("Prefer Bike")
    
elif Distance >= 15 :
    print("Prefer Car")