class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

student = Student(name, age, marks)

print(f"Name: {student.name}")
print(f"Age: {student.age}")
print(f"Marks: {student.marks}")
print(f"Result: {student.result()}")