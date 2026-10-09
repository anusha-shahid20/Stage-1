cart = []

while True:
    print("\n--- Shopping Cart ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        cart.append(item)
        print(f"'{item}' added to cart.")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print(f"'{item}' removed from cart.")
        else:
            print(f"'{item}' not found in cart.")

    elif choice == "3":
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print(f"Cart items: {cart}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")