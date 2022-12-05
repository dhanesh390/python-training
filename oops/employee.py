from abc import ABC


class Employee:
    """ This class represents the attributes of the employee object"""
    # Class variable
    company_name = 'Ides2it'

    # first constructor
    def __init__(self, name, role):
        self.name = name
        self.role = role

    """ 
     Python does not allow constructor overloading, it will take the last declared constructor 
     and will throw error if the sequence of arguments doesn't match to the last constructor
    """

    # second constructor to initialize the object
    def __init__(self, first_name, last_name, date_of_joining, role):
        self.first_name = first_name
        self.last_name = last_name  # Instance variable
        self.date_of_birth = date_of_joining
        self.role = role

    # Instance method
    def display(self):
        """ This displays the basic details of an employee"""
        return f'Employee {self.first_name} {self.last_name} works as a {self.role} in {Employee.company_name}'

    @staticmethod
    def calculate_age(date_of_birth):
        pass


class Developer(Employee):
    pass


class Tester(Employee):
    pass


# first_employee = Employee('dhanesh', 'developer')
# print(first_employee)
second_employee = Employee('Dhanesh', 'Kumar', '11.07.22', 'developer')
print(second_employee.display())


class Salary(ABC):
    def calculate_salary(self):
        pass
