from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import ChainMap
from collections import UserDict
from collections import UserString
from collections import UserList

# -> Default dict
# sample_list = defaultdict(str)
# sample_list['Dhanesh'] = 'Developer'
# sample_list['Deepak'] = 'Tester'
#
# print('1: ', sample_list)
#
# print(sample_list['Gowtham'])
# print('2: ', sample_list)
#
# sample_list.pop('Deepak')
# print('\n3: ', sample_list)
#
# sample_list['Deepak'] = 'Developer'
# print('\n4: ', sample_list)
#
# # Ordered dict ->
#
# sample_list = OrderedDict()
# sample_list['Dhanesh'] = 'Developer'
# sample_list['Deepak'] = 'Tester'
# sample_list['Gowtham'] = 'Developer'
#
# print('\n1.1: ', sample_list)
#
# sample_list.move_to_end('Deepak')
# print('\n1.2: ', sample_list)
#
# sample_list.move_to_end('Gowtham', last=False)
# print('\n1.3: ', sample_list)

# def test_counter():
#     c = Counter()
#     for i in range(10):
#         c[i] = 1
#     print(c)
#
#
# test_counter()
#
#
# def _test_default_dict():
#     d = defaultdict(int)
#     for i in range(10):
#         d[i] = 1
#     print(d)
#
#
# _test_default_dict()

# first_sample = {'1': 'Dhanesh', '2': 'Deepak', '3': 'Gowtham'}
# second_sample = {'4': 'Bala', '5': 'Hari', '1': 'Siva'}
#
# final_sample = ChainMap(first_sample, second_sample)
# print('3: ', final_sample)
#
# print('3.1: ', final_sample['1'])


# class CustomUserDict(UserDict):
#     def __setitem__(self, key, value):
#         key = str(key).lower()
#         self.data[key] = value
#
#     def __getitem__(self, key):
#         key = str(key).lower()
#         return self.data[key]
#
#
# custom_dict = CustomUserDict({'Name': 'Nik', 'Age': 33, 3: 3})
# print(f'userDict: {custom_dict["Age"]}')


class Employee(UserDict, UserString):

    def __init__(self):
        """ Will contain the class instance attributes"""
        super().__init__()
        super(UserDict, self).__init__(UserString)
        self.name = {}

    def set_name_(self, key, name):
        key = str(key).lower()
        self.name[key] = name

    def get_name_(self, key):
        key = str(key).lower()
        name = ''
        value = self.name[key]
        for i in range(len(value)):
            if i == 0:
                name += value[i].upper()
            else:
                name += value[i].lower()
        return name


dhanesh = Employee()
dhanesh.set_name_('name', 'dhanESh')
print('1: ', dhanesh.get_name_('name'))


class NumbersOnly(UserList):
    def __init__(self, iterable):
        super().__init__(
            item for item in iterable if type(item) in [int, float])

    def __setitem__(self, index, item):
        if type(item) in [int, float]:
            self.data[index] = item
        else:
            raise TypeError('Item must be a number.')

    def append(self, item):
        if type(item) in [int, float]:
            self.data.append(item)
        else:
            raise TypeError('Item must be a number.')

    def square_values(self):
        values = [item**2 for item in self.data]
        return values


sample_list = NumbersOnly([1, 2, 3, 'python'])

print('2: ', sample_list)
print('3: ', sample_list.square_values())

