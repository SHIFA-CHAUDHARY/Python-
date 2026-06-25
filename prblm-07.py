order_size = input("Enter Your Order size ( Small/Medium/Large)")
extra_shot = input("You Need Extra shot(YES/NO)")

if extra_shot == "Yes" :
    Coffee = order_size + " coffee with an Extra_shot"
    
else:
    Coffee = order_size + " Coffee"
    
print(Coffee)
    