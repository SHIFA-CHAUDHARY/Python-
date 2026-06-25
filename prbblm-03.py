Marks = int(input("enter Your marks"))
if Marks >= 101:
 print("Please verify Your Grade")
 exit()
 
 
if  Marks <= 100 and Marks >= 90:
     print('You have achieved Score "A"')
    
elif Marks<90 and Marks >=80:
    print('You have Achieved Score "B"')
elif Marks<80 and Marks >=70:
    print('You have achieved Score "C"')
    
elif Marks<70 and Marks >=60:
    print('You have achieved Score "D"')
    
else:
    print('You have achieved Score "F"')