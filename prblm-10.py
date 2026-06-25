Pet_age = int(input("Enter Your pet age:"))
Pet_specie =input("Enter Your Pet specie (Dog/Cat)")

if Pet_age <2 and Pet_age == "Dog":
    print("Give Your Dog 'Puppy Food' ")
    
elif Pet_age >5 and Pet_specie == "Cat" :
    print("Give Your cat 'senior Cat Food' ")
    
else:
    print("data not found")