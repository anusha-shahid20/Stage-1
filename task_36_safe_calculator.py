num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

try:
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")