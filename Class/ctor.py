class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, i am {self.name}")


john = Person("John Smith")
john.talk()

john_talking = "Are you there? John Smith is talking"
print(john_talking)
