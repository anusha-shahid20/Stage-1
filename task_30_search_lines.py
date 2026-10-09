word = input("Enter word to search: ")

with open("sample.txt", "r") as file:
    for line in file:
        if word in line:
            print(line.strip())