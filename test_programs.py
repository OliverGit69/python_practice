# Ask the user for a number and determine whether it is a prime number using a loop.sx

num = int(input("Please Enter a Number: "))
if num <= 1:
    print(f"Number {num} is Not a Prime")
for i in range(1, num + 1):
    if i != 1 and i != num and num % i == 0:
        print(f"{num} is Not a Prime Number")
        break
else:
   print(f"{num} is a Prime Number")