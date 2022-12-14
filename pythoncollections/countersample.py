from collections import Counter
from collections import UserString
import re

#
# a_list = [1, 2, 2, 3, 4, 4, 4]
# a_string = 'data'
# a_dict = {'a': 5, 'b': 3, 'c': 5, 'd': 5, 'e': 1}
#
# # Counting objects in a list
# c_list = Counter(a_list)
#
# # Counting characters in a string
# c_string = Counter(a_string)
#
# # Counting values in a dictionary
# c_dict = Counter(a_dict.values())
#
# print('counter list: ', c_list)
# print('counter_strinf: ', c_string)
# print('dict counter: ', c_dict)
# first_list = [1, 2, 2, 3, 4, 3, 2, 1, 2, 4, 5, 6, 5]
# c = Counter(first_list)
# print('\n1: ', c)
#
# c.update({2: 2, 7: 4})
# print('\n2: ', c)
#
# c.update({7: 1, 2: 1})
# print('\n3: ', c)
#
# c.update({8: 2, 2: 1})
# print('\n4: ', c)
#
# print('\n5: ', c[4])
#
# c.update('Pythoon')
# print('\n6: ', c)
#
# print('\n7: ', c.most_common(4))
#
# # c.clear()
# # print('\n8: ', c)
#
# print('\n8.1: ', list(c.elements()))
#
# second_list = [1, 2, 3, 4]
# d = Counter(second_list)
# print('\n9: ', d)
#
# print('\n10: ', c + d)
#
# print('\n11: ', c.__add__(d))
#
# print('\n12: ', c & d)
#
# print('\n13: ', c | d)

# first_string = 'appddresadsbtrntrfedewvc'
# second_string = 'svtrbndsvl'
#
# first_counter = Counter(first_string)
# for i in second_string:
#     print(f' {i} : {first_counter[i]}')

list_of_employees = []


class Employee(UserString):

    def __init__(self, seq: object):
        super().__init__(seq)
        self.name = None

    def set_name(self, name):
        employee_name = Employee.validate_name(name)
        self.name = employee_name
        # name = re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name)

    def get_name(self):
        return self.name

    @staticmethod
    def validate_name(value):
        result = re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', value)
        if result:
            return result
        else:
            print(f'Invalid name {value}')


def add():
    pass


def _init():
    is_continue = True
    while is_continue:
        print('Enter 1 to add\nEnter 2 to view')

        user_choice = int(input('Enter your choice: '))
        match user_choice:
            case 1:
                add()


if __name__ == '__main__':
    _init()
