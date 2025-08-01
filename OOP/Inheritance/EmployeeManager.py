# Create a class Employee and a class Manager that inherits from it. Add an extra property team_size in Manager and override the method to show details.
class Employee:
    def __init__(self, dev_salary = 0):
        self.dev_salary = dev_salary

    def dev_dic(self, salary):
        try:
            dev_salary = {
                "React": 2000,
                "Python": 3000,
                "Java": 4000,
                "C++": 5000,
                "C#": 6000
            }
            salaries = dev_salary.get(salary, "Invalid search")
            return salaries
        except Exception as ex:
            print(f"Error: {ex}")


class Manager(Employee):
    def __init__(self, team_size = 0 , dev_salary = 0):
        super().__init__(dev_salary)
        self.team_size = team_size

    def dev_dic(self, team):
        try:
            dev_team = {
                "React": 2,
                "Python": 3,
                "Java": 4,
                "C++": 5,
                "C#": 6,
            }
            teams = dev_team.get(team, "Invalid search")
            return teams

        except Exception as ex:
            print(f"Error: {ex}")

    def salary(self):
        language = input("Which language salary do you want to know? ")
        salary = super().dev_dic(language)
        print(f"Salary: {salary} of the {language} language")

        team_size = self.dev_dic(language)
        print(f"Team size: {team_size} of the {language} language")


Obj_Manager = Manager()
Obj_Manager.salary()
