from abc import ABC, abstractmethod
from datetime import date


class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def calculate_age(date_of_birth):
        today = date.today().isoweekday()
        return today


class Trainee(Employee):

    def __init__(self, training_model, name, age):
        super().__init__(name, age)
        self.training_model = training_model

    def __repr__(self):
        return self.name

    # @staticmethod
    # def calculate_age(date_of_birth):
    #     today = date.today().isoweekday()
    #     return today


class Trainer(Employee):

    def __init__(self, projects, name, age):
        super().__init__(name, age)
        self.projects = projects

    # @staticmethod
    # def calculate_age(date_of_birth):
    #     today = date.today().isoweekday()
    #     return today


class Management(Trainee):

    def __init__(self, salary, training_model, name, age):
        super().__init__(training_model, name, age)
        self.salary = salary

    def __repr__(self):
        value = self.calculate_age(12)
        return str(value)


new_employee = Management(2000, 'python', 'dhanesh', 22)

print(new_employee.calculate_age(23))

print(new_employee)
