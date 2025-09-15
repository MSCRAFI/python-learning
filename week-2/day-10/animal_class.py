# python program to demonstrate inheritance in OOP

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."
    
class Dog(Animal):
    def fetch(self):
        return f"{self.name} says Woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Buddy makes a sound.
print(dog.fetch())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!