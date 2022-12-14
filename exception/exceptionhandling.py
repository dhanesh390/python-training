from collections import OrderedDict
# print(len(dir(locals()['__builtins__'])))
# print(dir(locals()['__builtins__']))


class InvalidInput(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'{self.message}'
        else:
            return 'Invalid input'


employee_dict = OrderedDict()


def get_input():
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    salary = float(input('Enter your salary: '))
    employee_id = input('Enter your id: ')
    employee_dict[employee_id] = [name, age, salary]

    return employee_dict


def _init_():
    is_continue = True
    while is_continue:
        try:
            print('Enter 1 to get input\nEnter 2 to display\nEnter 3 to exit')
            user_choice = int(input('Enter your choice: '))
            if user_choice <= 0:
                raise InvalidInput('Please provide a valid value')
        except (InvalidInput, TypeError, ValueError) as exception:
            print(f'Invalid data type provided:  {exception}')
        else:
            match user_choice:
                case 1:
                    get_input()
                case 2:
                    print(employee_dict)
                case 3:
                    is_continue = False
                case _:
                    print('Invalid input')
        finally:
            print('function proceeds')


if __name__ == '__main__':
    _init_()


# class CustomError(Exception):
#     """Base class exception for all the exceptions of this module"""
#     pass
#
#
# class InputIsNegativeError(CustomError):
#     """Raised when User enters a negative value"""
#     pass
#
#
# if __name__ == '__main__':
#     try:
#         value = int(input("Input a number: "))
#         if value < 0:
#             raise InputIsNegativeError
#     except InputIsNegativeError:
#         print("Input value shouldn't be negative")

