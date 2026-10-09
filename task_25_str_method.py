class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Marks: {self.marks}"


name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

student = Student(name, age, marks)

print(student)