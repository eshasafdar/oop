class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 2)

dog1.bark()
dog2.bark()
