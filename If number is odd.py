""" Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user.
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

n = int(input("Give me a number to check:"))
print("Your check number is", n)
div = int(input("Give me a number to divide by:"))
print("Your number to divide is:", div)

if n > 4 and n % 4 == 0:
    print("Your number is a multiple of 4")
elif n % 2 == 0:
    print("Your number is not odd")
else:
    print("Your number is odd")

if n % div == 0:
    print(n,"devides by",div)
else:
    print(n,"does not divide by", div)
