ch = input("Enter any string : ")

if ch.isupper():
    print(f"{ch} is Capital letters")

elif ch.islower():
    print(f"{ch} is Small letters")   
    
elif ch.isdigit():
    print(f"{ch} is Digit")     

elif ch.isspace():
    print(f"{ch} is blank Space") 
    
else :
    print(f"{ch} is Special Charcater ")       