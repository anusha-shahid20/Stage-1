numbers = [45, 12, 78, 3, 99, 23, 56]

# Using built-in functions
print(f"Largest (using max): {max(numbers)}")
print(f"Smallest (using min): {min(numbers)}")

# Without using max() and min()
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print(f"Largest (manual): {largest}")
print(f"Smallest (manual): {smallest}")