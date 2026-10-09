with open("sample.txt", "r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()

print(f"Number of lines: {len(lines)}")
print(f"Number of words: {len(words)}")