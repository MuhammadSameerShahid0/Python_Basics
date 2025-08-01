#Create a class Animal with a method make_sound(). Inherit two classes Dog and Cat and override the sound method in both.

class Animal:
    def make_sound(self):
        print("Animals making the noise")

class Dog(Animal):
    @classmethod
    def make_sound(cls):
        print("Dogs making the noise")

class Cat(Animal):
    def make_sound(self):
        print("Cats making the noise")

cat = Cat()
dog = Dog()

cat.make_sound()
Dog.make_sound()