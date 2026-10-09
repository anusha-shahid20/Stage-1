while True:
    try:
        num = float(input("Enter a number: "))
        print(f"You entered: {num}")
        break
    except ValueError:
        print("That's not a valid number. Try again.")