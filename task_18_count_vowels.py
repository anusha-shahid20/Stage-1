def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count = count + 1
    return count

text = input("Enter a string: ")
result = count_vowels(text)

print(f"Number of vowels: {result}")