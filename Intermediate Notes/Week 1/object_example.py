class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Some random sound"

    def info(self):
        return f"{self.name} is {self.age} years old."
    
random_animal = Animal("Deer", 2)
random_animal2 = Animal("Frog", 4)

print(random_animal2.info())
print(random_animal2.speak())

class DogInherit(Animal):
    def speak(self):    # Override the speak method
        return ("Woof!")

class CatInherit(Animal):
    def speak(self):    # Override the speak method
        return "Meow!"


dog1 = DogInherit("Buddy", 5)
cat1 = CatInherit("Whiskers", 3)

print(dog1.info())      # From Animal class
print(dog1.speak())     # Overridden in Dog class

print(cat1.info())      # Inherited from Animal
print(cat1.speak())     # Overridden in Cat


"""
Using super() to call the parent class method - can be used to inherit and extend functionality. 
Note: This is used when you want to to define extra attributes in child class
"""

class DogInheritUsingSuper(Animal):
    def __init__(self, name, age, breed="Unknown"):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        parent_sound = super().speak()  # Call the parent class method
        return parent_sound + " Woof!"
    

print("\n----- Using super() -----\n")

dog2 = DogInheritUsingSuper("Max", 4) # Uses default breed which is "Uknown"

print(dog2.info())
print(dog2.breed)
print(dog2.speak())

print("\n-----\n")

dog3 = DogInheritUsingSuper("Rex", 6, "German Shepherd")

print(dog3.info())
print(dog3.breed)
print(dog3.speak())     # Overridden in DogInheritUsingSuper class
