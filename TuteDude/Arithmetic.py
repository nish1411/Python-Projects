number1 = int(input("Enter 1st no: "))
number2 = int(input("Enter 2nd no: "))

Add = number1 + number2
Sub = number1 - number2
Mul = number1 * number2

# Handling division to prevent ZeroDivisionError
if number2 != 0:
    Div = number1 / number2
else:
    Div = "Undefined (cannot divide by zero)"



print (f"The Addition of {number1} & {number2} is",Add)
print (f"The Subtraction of {number1} & {number2} is",Sub)
print (f"The Multiplication of {number1} & {number2} is",Mul)
print (f"The Division of {number1} & {number2} is",Div)