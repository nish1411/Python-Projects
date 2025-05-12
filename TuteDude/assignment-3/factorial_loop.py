n = int(input("Enter a number: "))
num = n

for i in range(n,1,-1):
    n=n*(i-1)

print (f"Factorial of {num} is:", n)

