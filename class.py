class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I'am {self.name}")

john = Person("John Smith")
john.talk()
bob = Person("Bob Smith")
bob.talk()

class Mammal:
    def walk(self):
        print("Walk")

class dog(Mammal):
    def bark(self):
        print("bark")

class cat(Mammal):
    def meow(self):
        print("meoww")

dog1 = dog()
dog1.walk()
dog1.bark()
cat1 = cat()
cat1.walk()
cat1.meow()