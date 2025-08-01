#Create a class Person with properties like name and age. Inherit a class Student that adds student_id and a method to display student info.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def person_details(cls, name, age):
        try:
            print(f"Name: {name}, Age: {age}")
        except Exception as ex:
            print(f"Exception occurs: {ex}")


class Student(Person):
    def __init__(self, name, age, student_id):
        try:
            super().__init__(name, age)
            self.student_id = student_id
        except Exception as ex:
            print(f"Exception occurs: {ex}")

    def student_info(self):
        try:
            print(f"Name: {self.name}, Age: {self.age}, student_id: {self.student_id}")
        except Exception as ex:
            print(f"Exception occurs: {ex}")


student_details = Student("John", 20, 1)
student_details.student_info()
