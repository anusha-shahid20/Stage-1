students = {
    "Ali": 85,
    "Sara": 92,
    "Bilal": 78,
    "Hina": 88,
    "Usman": 95
}

total = 0

for name in students:
    total = total + students[name]

average = total / len(students)

print(f"Marks: {students}")
print(f"Total: {total}")
print(f"Average: {average}")