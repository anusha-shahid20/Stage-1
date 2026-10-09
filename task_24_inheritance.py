class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def sound(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def sound(self):
        print(f"{self.name} says Meow!")


dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.sound()
cat.sound()