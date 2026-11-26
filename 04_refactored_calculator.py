# Refactored Calculator Program
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result =", add(num1, num2))
elif operator == "-":
    print("Result =", subtract(num1, num2))
elif operator == "*":
    print("Result =", multiply(num1, num2))
elif operator == "/":
    print("Result =", divide(num1, num2))
else:
    print("Invalid operator")
