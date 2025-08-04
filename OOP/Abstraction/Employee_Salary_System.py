# Make an abstract class Employee with method calculate_salary(). Implement FullTimeEmployee and PartTimeEmployee with their own salary logic.
from abc import abstractmethod, ABC


class Employee(ABC):
    def __init__(self, salary = 0):
        self.salary = salary

    @abstractmethod
    def calculate_salary(self):
        return self.salary


class FullTimeEmployee(Employee):
    def __init__(self, salary):
        super().__init__(salary)

    def calculate_salary(self):
        self.salary += 100
        print(f"The employee has a full time salary. {self.salary}")


class PartTimeEmployee(Employee):
    def __init__(self, salary):
        super().__init__(salary)

    def calculate_salary(self):
        self.salary += 50
        print(f"The employee has a part time salary. {self.salary}")


class CalculateSalary:
    @classmethod
    def calculate(cls):
        while True:
            employee_time = input("Choose: [1] PartTimeEmployee , [2] FullTimeEmployee, [3] Exit: ")
            match employee_time:
                case "1":
                    part_time = PartTimeEmployee(500)
                    part_time.calculate_salary()
                case "2":
                    full_time = FullTimeEmployee(1000)
                    full_time.calculate_salary()
                case "3":
                    print("Exit...")
                    break
                case _:
                    print(f"Invalid input: {employee_time}")


calculate_salary = CalculateSalary()
CalculateSalary.calculate()