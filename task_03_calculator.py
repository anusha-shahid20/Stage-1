num1 = float(input("Enter first number: "))


num2 = float(input("Enter second number: "))

sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2

print()  
print("Results:")
print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {diff_result}")
print(f"{num1} * {num2} = {product_result}")
if num2 != 0:
    quotient_result = num1 / num2
    print(f"{num1} / {num2} = {quotient_result}")
else:
    print(f"{num1} / {num2} = Cannot divide by zero")