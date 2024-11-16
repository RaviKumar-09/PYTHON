class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Create object
person1 = Person("Ravikumar", 25)
person1.greet()  # Output: Hello, my name is Ravikumar.
