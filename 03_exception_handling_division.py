# Exception Handling Division Program
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
    print("Division =", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
