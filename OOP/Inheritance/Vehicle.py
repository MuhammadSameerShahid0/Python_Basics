#Create a class Vehicle with a method start_engine(). Inherit a class Car that overrides the method and adds model.

class Vehicle:
    def start_engine(self):
        print("Start Engine")

class Car(Vehicle):
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        print(f"Engine Start {self.model}")

car = Car("BMW")
car.start_engine()