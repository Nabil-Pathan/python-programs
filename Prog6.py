# def display_even(numbers):
#     even_numbers = [num for num in numbers if num % 2 == 0]
#     print("Even Numbers : ",even_numbers)

# numbers = [1,2,3,4,5,6,7,8,9]

# display_even(numbers)

# Calculate NCR


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def ncr(n,r):
    return factorial(n) // (factorial(r) * factorial(n-r))

n = 5 
r = 2

print(ncr(n,r))




    