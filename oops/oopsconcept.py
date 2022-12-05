from abc import abstractmethod
from datetime import date


class Employee:
    """ This class represents the employee class object"""
    company_name = 'Ideas2it'

    # Parametrized constructor for the employee instance object
    def __init__(self, first_name='', last_name='', employee_id='', role=''):
        self.__experience = None
        self.__age = None
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.role = role

    def set_date_of_birth(self, date_of_birth):
        """ This method is used to calculate age from date of birth """
        today = date.today()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        self.__age = age

    def get_age(self):
        """ Returns the age of the employee """
        return self.__age

    def set_date_of_joining(self, date_of_joining):
        """ This method is used to calculate the experience from date of joining """
        today = date.today()
        experience = today.year - date_of_joining.year - (
                (today.month, today.day) < (date_of_joining.month, date_of_joining.day))
        self.__experience = experience

    def get_experience(self):
        """ Returns the experience of the employee """
        return self.__experience

    @staticmethod
    def set_salary(salary):
        pass

    def __repr__(self):
        return f'Welcome {self.first_name} {self.last_name} to {self.company_name}'

    @abstractmethod
    def __del__(self):
        """ Destructor method which will delete the reference object once the reference counter hits Zero"""
        return f'employee object has been deleted'


class Trainee(Employee):
    employee_title = 'Trainee'

    def __init__(self, first_name='', last_name='', employee_id='', role=''):
        super().__init__(first_name, last_name, employee_id, role)
        self.period_of_training = None
        self.employee_title = Trainee.employee_title

    def set_period_of_training(self, period_of_training):
        self.period_of_training = period_of_training

    def get_period_of_training(self):
        return self.period_of_training

    def __del__(self):
        """ Destructor method which will delete the reference object once the reference counter hits Zero"""
        return f'employee object has been deleted'


class Trainer(Employee):
    employee_title = 'Trainer'

    def __init__(self, first_name='', last_name='', employee_id='', role=''):
        super().__init__(first_name, last_name, employee_id, role)
        self.no_of_projects = None

    def set_projects_worked(self, no_of_projects=0):
        self.no_of_projects = no_of_projects

    def get_projects_worked(self):
        return self.no_of_projects

    def __del__(self):
        """ Destructor method which will delete the reference object once the reference counter hits Zero"""
        return f'employee object has been deleted'


dhanesh = Trainee(first_name='Dhanesh', last_name='Kumar', employee_id='I2i01', role='Developer')
print(dhanesh)
justin = Trainer(first_name='Justin', last_name='Raj', employee_id='I2i02', role='Lead architect')
print(justin)
justin.set_salary(2000000)
justin.set_projects_worked(20)
print(justin.get_projects_worked())
#
#
# list_of_employees = {}
#
# _id = 1
#
#
# def add():
#     # new_employee = Employee()
#     first_name = input('Enter your first name: ')
#     last_name = input('Enter your last name: ')
#     global _id
#     employee_id = myconstants.COMPANY_ID + str(_id + 1)
#     role = input('Enter your role:  ')
#     date_of_birth = input('Enter your date of birth: ')
#     date_of_joining = input('Enter your date of joining: ')
#     new_employee = Employee(first_name, last_name, employee_id, role, date_of_birth, date_of_joining)
#     print(new_employee)
#     return new_employee# def _init():
# #     is_continue = True
# #     while is_continue:
# #         print('Enter 1 to add\nEnter 2 to view')
# #         user_input = input('Enter your choice: ')
# #         match user_input:
# #             case 1:
# #                 print(add())
# #
# #
# # if __name__ == '__main__':
# #     _init()
#
#
