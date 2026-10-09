name = input("Enter a name: ")

with open("contacts.txt", "a") as file:
    file.write(name + "\n")

print(f"'{name}' added to contacts.txt")

# Show current contacts
with open("contacts.txt", "r") as file:
    content = file.read()

print("\nCurrent contacts:")
print(content)