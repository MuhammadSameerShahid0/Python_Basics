# Create a class Calculator and Subclasses like Addition, Subtraction, Multiplication, and Division each perform a different operation.
from abc import abstractmethod, ABC


class Calculator(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def calculate(self):
        return self.amount


class Add(Calculator):
    def __init__(self, amount=0):
        super().__init__(amount)

    def calculate(self):
        first_amount = int(input("Enter first amount: "))
        second_amount = int(input("Enter second amount: "))
        amount = first_amount + second_amount
        self.amount = amount
        print("The new amount is: ", self.amount)


class Subtraction(Calculator):
    def __init__(self, amount=0):
        super().__init__(amount)

    def calculate(self):
        first_amount = int(input("Enter first amount: "))
        second_amount = int(input("Enter second amount: "))
        amount = first_amount - second_amount
        self.amount = amount
        print("The new amount is: ", self.amount)


class Multiplication(Calculator):
    def __init__(self, amount=0):
        super().__init__(amount)

    def calculate(self):
        first_amount = int(input("Enter first amount: "))
        second_amount = int(input("Enter second amount: "))
        amount = first_amount * second_amount
        self.amount = amount
        print("The new amount is: ", self.amount)


class Division(Calculator):
    def __init__(self, amount=0):
        super().__init__(amount)

    def calculate(self):
        first_amount = int(input("Enter first amount: "))
        second_amount = int(input("Enter second amount: "))
        amount = first_amount / second_amount
        self.amount = amount
        print("The new amount is: ", self.amount)


class Run:
    @classmethod
    def run(cls):
        operations = {
            "1": Add,
            "2": Subtraction,
            "3": Multiplication,
            "4": Division
        }

        while True:
            choice = input("Choose: [1] Add, [2] Subtract, [3] Multiplication, [4] Division, [5] Exit: ")
            if choice == "5":
                print("Exiting...")
                break
            elif choice in operations:
                operation_class = operations[choice]
                operation = operation_class()
                operation.calculate()
            else:
                print("Invalid option.")


runner = Run()
runner.run()
