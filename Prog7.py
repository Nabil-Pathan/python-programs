n = int(input("Enter n : "))

a = 0
b = 1
temp = 0 

while n > 0 :
    print(a , " ", end="")
    a = a+b
    temp = a
    a = b 
    b = temp
    n = n -1 