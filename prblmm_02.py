age = int(input("enter Your age:"))
day = input("enter your day:")

price = 12 if age >= 18 else 8
if day == "Wednesday":
    price = price - 2 

print("Ticket price for you is $" ,price)
