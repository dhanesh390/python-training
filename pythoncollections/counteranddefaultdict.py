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

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary


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
    """ This method returns a generated id for each employee created in a sequential order"""
    count = 0
    is_continue = True
    while is_continue:
        employee_id = 'i2i' + str(count)
        yield employee_id
        count += 1


ids = generate_id()


def add_technical_employee():
    """ This method creates a new employee object and stores them in a collection"""
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    salary = float(input('Enter your salary: '))
    role = input('Enter your role: ')
    projects_worked = int(input('No of projects worked: '))
    employee_id = next(ids)
    new_employee = TechnicalEmployee(name=name, age=age, salary=salary, role=role, projects_worked=projects_worked)
    list_of_employees[employee_id] = new_employee


file_path = os.getcwd()


def get_employee_id():
    """ Returns the employee id which users inputs"""
    employee_id = input('Enter employee id: ')
    if not isinstance(employee_id, str):
        raise TypeError('Invalid input')
    else:
        return employee_id

    # try:
    #     employee_id = input('Enter employee id: ')
    #     if not isinstance(employee_id, str):
    #         raise TypeError('Invalid input')
    # except TypeError as invalid_exception:
    #     print(f'Exception occurs due to {invalid_exception} ')
    # else:
    #     return employee_id


# def pf(function):
#     def calculate_pf(salary):
#         if salary >= 25000:
#             _pf = salary - (salary * 0.25)
#         elif 25000 < salary <= 50000:
#             _pf = salary - (salary * 0.35)
#         else:
#             _pf = salary - (salary * 0.45)
#         return function(salary, _pf)
#
#     return calculate_pf
#
#
# def insurance(function):
#     def calculate_insurance(salary, _pf):
#         _insurance = salary - (1508 + 208)
#         return function(salary, _pf, _insurance)
#     return calculate_insurance
#
#
# @pf
# @insurance
# def get_salary_slip(salary, _pf, _insurance):
#     return f'The employee gross salary is {salary} from that {_pf} of pf and {_insurance} will be deducted and your ' \
#            f'salary in hand will be {salary - (_pf + _insurance)} '


def salary_details():
    """ Returns the payslip of the employee"""
    employee_id = get_employee_id()
    try:
        current_employee = list_of_employees.get(employee_id)
    except KeyError as invalid_key_exception:
        print(f'No employees found for the key {employee_id} and thus {invalid_key_exception} occurs ')
    else:
        salary = current_employee.get_salary()
        # return get_salary_slip(salary=salary)
        return salary


def file_technical_employees():
    """ Store the employee records into a file in local storage in the particular file"""
    pass


def _init_():
    """ Method to initialize the entire operation of the employee management portal"""
    is_continue = True
    while is_continue:
        print('Enter 1 to add a Technical employee\nEnter 2 for Management employee\nEnter 3 to view Technical '
              'employees\nEnter 4 to get salary details')

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
                    get_employee_id()

                case 3:
                    print([{i: j.__dict__} for i, j in list_of_employees.items()])
                case 4:
                    salary_details()
                case 5:
                    file_technical_employees()
                case _:
                    print('Invalid input')
        finally:
            print('Request processed')


if __name__ == '__main__':
    try:
        _init_()
    except Exception as e:
        print(f'The exception occurs due to {e}')
