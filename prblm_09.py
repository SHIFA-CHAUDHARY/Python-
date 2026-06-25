Year = int(input("Enter a Year"))

if ( Year % 4 == 0  and Year % 100 != 0 ) or ( Year % 400 == 0 ) :
    print("Leap Year")
    
else :
    print("Normal Year")