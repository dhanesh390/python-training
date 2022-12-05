import functools

first_list = {1: 2, 2: 3, 3: 4, 4: 5}
second_list = (1, 2, 3, 4)
third_list = [1, 2]
fourth_variable = 'Java', 'python'
fifth_variable = 4


def add(a, b):
    return a + b


"""
 Zip function only takes iterables as input and returns a list
 It can take 0 arguments as well as n number of arguments
"""
print('Zip 1: ', list(zip(first_list, second_list, third_list)))

""" 
 Zip only takes iterables as input, it does not take single object 
 as input, it will throw an error. whereas other hands string are 
 iterable so even single string is approved as input 
"""
print('Zip 2: ', list(zip(first_list, fourth_variable)))

# print('Zip 3: ', list(zip(first_list, fifth_variable)))
"""
 Map takes arguments based on the function provided it works similar
 to zip function only works until the least iterable object provided in the lists
"""
print('map 1: ', list(map(add, first_list, second_list)))
print('zip 0.0: ', list(zip(third_list, map(add, first_list, second_list))))
# print('map 0: ', list(map(add, zip(first_list, second_list), third_list)))

""" 
 Similar to zip function, Map function also does not take single 
 value object as input as it only takes iterables 
 """
# print('map 2: ', list(map(add, first_list, fourth_variable)))

# print('map 3: ', list(map(add, first_list, fifth_variable)))

sample_list = [1, 2, 3, 4, 5, 6]


def is_even(b):
    """ Checks whether the input value is even and returns according to the call"""
    return b % 2 == 0


print('zip 4: ', list(zip(first_list, filter(is_even, second_list))))
print('zip 4.1: ', list(zip(first_list, filter(is_even, map(add, first_list, second_list)))))
""" 
 Filter function takes a function and iterable as argument 
 and return the value which return values that checks the condition
"""
filtered_list = filter(is_even, sample_list)
print('filter type: ', type(filtered_list))
print('filter 1: ', set(filtered_list))
mapped_list = map(is_even, sample_list)
print('map 3: ', list(mapped_list))
'''
 Even filter does not take single value as input
'''
filtered_list_two = filter(is_even, fourth_variable)

filter_list_three = filter(is_even, map(add, first_list, second_list))


# filter_list_four = filter(is_even, map(add, zip(first_list, second_list), third_list))
# print('fiter map zip: ', list(filter_list_four))

print('filter 0: ', list(filter_list_three))
# print('filter 2: ', list(filtered_list_two))
"""
 Where as when the same is called in map it returns the entire values 
 as boolean values for the whole arguments 
"""
 # Check for multiple variables
print('mapped type: ', type(mapped_list))


"""
 Reduce function takes a iterable as input along with a function 
 And returns a single value as output
"""
reduce_list = functools.reduce(add, first_list)
print('filter reduce map: ', functools.reduce(add, filter(is_even, map(add, first_list, second_list))))
print('reduce type: ', type(reduce_list))
print('reduce 1: ', reduce_list)

reduct_list = functools.reduce(add, fourth_variable)
print('reduce type for String: ', type(reduct_list))
print('reduce 2: ', reduct_list)

""" It throws a type error as the reduce function here returns int """
# reduce_first_list = zip(second_list, functools.reduce(add, first_list))
# print('reduced zip 1: ', reduce_first_list)

#  Reduce doesn't work with int types whereas it works for other iterables
reduce_second_list = zip(second_list, functools.reduce(add, fourth_variable))
print('reduced zip 2: ', list(reduce_second_list))


# reduce_first_list = map(add, second_list, functools.reduce(add, first_list))
# print('reduced zip 3: ', reduce_first_list)


def add(a, b):
    return str(a) + str(b)


reduce_second_map = map(add, second_list, functools.reduce(add, fourth_variable))
print('reduced zip 4: ', list(reduce_second_map))

# reduced_list = functools.reduce(add, fifth_variable)
# print('reduce 3: ', reduced_list)

"""
 Four types of argument passing Default(b= 30) , Positional ( 2, 3), 
 keyword ( b = 20, c = 20) and arbitrary arguments
 ( / ) variables before this should only be positional remaining can be positional or keyword
 ( * ) variables after this are only should be keyword arguments
"""

""" 
 Method containing all the types of argument passing 
 like positional, keyword, de
"""

"""
 Arguments passed always works on tuple unpacking which always check the values along with the parameters
 
 Can never give defaut values in the first place 
"""


def add(a, b, /, c=4, *, d=4):
    return a + b + c + d


print('Arguents: ', add(3, 4, 1, d=2))


def percentage(*subjects):
    """ Arbitrary positional argument"""
    total = 0
    for i in subjects:
        total = total + i
    avg = total / len(subjects)
    return avg


print('* arguments: ', percentage(56, 61, 73).__round__(2))
print(type(percentage(56, 61, 73).__round__(2)))


def percentage(**mark_list):
    """ Arbitrary positional argument"""
    percentage_list = {}
    for sub in mark_list:
        percentage_list[sub] = mark_list[sub]
    return percentage_list


print('** Arguments: ', percentage(math=56, english=61, science=73))
print(type(percentage(math=56, english=61, science=73)))

# lambda argument: expression
sam_list = list(map(lambda a: a ** 2, range(10)))
sam_list2 = [a ** 2 for a in range(10)]
print('sam1: ', sam_list)
print('sam2: ', sam_list2)

"""
 Enumneration adds a counter to the iterable passed as argument and returns a tuple
"""
enumarated_list = enumerate(sam_list)
print('Enumerated list 1: ', tuple(enumarated_list))
# check for reverse keys - cannot reverse as it is a  generator which cannot be reversed
enumarated_list = enumerate(sam_list, 1000)
print('Enumerated list 2: ', tuple(enumarated_list))

enumnerate_string = enumerate(fourth_variable)
print('enumeratestring: ', list(enumnerate_string))

"""
 Enumerate function also expects a iterable as input does not take single value as input
"""
# enumnerate = enumerate(fifth_variable)
# print('Enumerate object: ', enumnerate)

list_of_employees = ['Dhanesh', 'Gowtham', 'Deepak', 'Hari']
weekly_time_sheet = [[8, 8, 9, 7, 6, 8], [8, 8, 7, 8, 9, 8], [8, 8, 9, 7, 6, 8], [8, 8, 9, 7, 6, 8], [8, 8, 9, 7, 6, 8]]

employee_time_sheet = zip(list_of_employees, weekly_time_sheet)
print(type(employee_time_sheet))
print('Zip of : ', dict(employee_time_sheet))

no_of_employees = enumerate(list_of_employees, 100)
print('enumerated list: ', tuple(no_of_employees))


def add(a, b):
    return a + b


employee_working_hours = functools.reduce(add, weekly_time_sheet)
print('Working hours: ', list(employee_working_hours))

global_variable = 10


def my_function():
    #global global_variable
    # global_variable = 20
    # global_variable += 2
    local_variable = 15
    print('1', global_variable)
    print('2', local_variable)


my_function()
print('3', global_variable)

# employees_list = [['Dhanesh', 'Tester'], ['Gowtham', 'Developer'], ['Deepak', 'Developer']]
#
# greeting = lambda employee : print(f'Welcome {employee[0]}')
#
# welcome_employees = map(greeting, employees_list)
# print('lambda map: ', list(welcome_employees))

enum_list = [['a', 'b'], {'c', 'd'}]
print('enum nested list: ', list(enumerate(enum_list)))

enum_dictionary = {1: 'a', 2: 'b', 3: 'c'}
print('enum dict: ', list(enumerate(enum_dictionary)))


#  Recursion function (which calls itself again and again whenever called)


def factorial(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        return x * factorial(x - 1)


num = 0
print(f'The factorial of {num} is {factorial(num)}')

default_list = [1, 2, 3, 4, 5, 6]


def is_accurate(a):
    if a % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


print('map using filter fun 5: ', list(map(is_accurate, default_list)))
print('Filter using filter fun 6: ', list(filter(is_accurate, default_list)))


# def tower_of_hanoi(n, source, destination, auxiliary):
#     if n == 1:
#         print("Move disk 1 from source", source, "to destination", destination)
#         return
#     tower_of_hanoi(n - 1, source, auxiliary, destination)
#     print("Move disk", n, "from source", source, "to destination", destination)
#     tower_of_hanoi(n - 1, auxiliary, destination, source)
#
#
# n = 3
# tower_of_hanoi(n, 'A', 'B', 'C')
