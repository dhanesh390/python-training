from abc import ABC
from abc import abstractmethod
from collections import Counter
from collections import ChainMap
from collections import defaultdict
from collections import namedtuple
from exception import exceptionhandling
import os


class Company(ABC):
    company_name = 'ideas2it'

    def __init__(self, name: str = '', age: int = 0, salary: float = 0.0):
        self.name = name
        self.age = age
        self.salary = salary

    @abstractmethod
    def __str__(self):
        return f'Welcome {self.name} to {Company.company_name}'


class TechnicalEmployee(Company):

    def __init__(self, name: str = '', age: int = 0, salary: float = 0.0, role: str = '', projects_worked: int = 0):
        super().__init__(name, age, salary)
        self.role = role
        self.projects_worked = projects_worked

    def __str__(self):
        return f'Welcome {self.name} to {Company.company_name} as {self.role}'


class ManagementEmployee(Company):

    def __init__(self, name: str = '', age: int = 0, salary: float = 0.0, department: str = ''):
        super().__init__(name, age, salary)
        self.department = department

    def __str__(self):
        return f'Welcome {self.name} to {Company.company_name} to the {self.department} department'


list_of_employees = defaultdict(Company)


def generate_id():
    count = 0
    is_continue = True
    while is_continue:
        employee_id = 'i2i' + str(count)
        yield employee_id
        count += 1


ids = generate_id()


def add_technical_employee():
    # employees = {}
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    salary = float(input('Enter your salary: '))
    role = input('Enter your role: ')
    projects_worked = int(input('No of projects worked: '))
    employee_id = next(ids)
    new_employee = TechnicalEmployee(name=name, age=age, salary=salary, role=role, projects_worked=projects_worked)
    # employees[employee_id] = new_employee
    list_of_employees[employee_id] = new_employee

file_path = os.getcwd()
def file_technical_employees():
    pass


def _init_():
    is_continue = True
    while is_continue:
        print('Enter 1 to add a Technical employee\nEnter 2 for Management employee\nEnter 3 to view Technical '
              'employees')

        try:
            user_choice = int(input('Enter your choice: '))
            if not str(user_choice).isnumeric():
                raise exceptionhandling.InvalidInput('1: Invalid input')
        except exceptionhandling.InvalidInput as invalid_exception:
            print(f'2: Exception occurs due to {invalid_exception}')
        except TypeError as type_exception:
            print(f'3: Invalid type of input {type_exception}')
        except ValueError as value_exception:
            print(f'4: Invalid value for input {value_exception}')
        else:
            match user_choice:
                case 1:
                    add_technical_employee()
                case 2:
                    pass
                case 3:
                    print([{i: j.__dict__} for i, j in list_of_employees.items()])
                case 5:
                    file_technical_employees()
                case _:
                    print('Invalid input')
        finally:
            print('Request processed')


if __name__ == '__main__':
    _init_()


