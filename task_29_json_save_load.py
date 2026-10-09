import json

student = {
    "name": "Anusha",
    "age": 20,
    "marks": 85,
    "courses": ["Python", "Math", "English"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Saved to student.json")

with open("student.json", "r") as file:
    loaded = json.load(file)

print("\nLoaded data:")
print(loaded)
print(f"\nName: {loaded['name']}")
print(f"Age: {loaded['age']}")