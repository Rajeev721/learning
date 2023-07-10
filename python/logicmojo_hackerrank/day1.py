# Using Recursion
# write a program to find power of a number
# Find factorial of a number

# Iteration
# Find if the string is palindrome
# find if an integer is a prime number or not
def prim(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
            else:
                print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

prim(17)