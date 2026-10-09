def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return f"Age is valid: {age}"


try:
    age = int(input("Enter your age: "))
    result = check_age(age)
    print(result)
except ValueError as e:
    print(f"Error: {e}")