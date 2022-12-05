# Start of the python demo

# Naming conventions

# Variable naming should be in lower case and be meaning full

# first_number = input("Enter the first number: ")
# second_number = input("Enter the second number: ")

# function names should be only in lower case $ if multiple name use underscore
# two line spaces should be provided between functions


# def my_function():
#     # four white spaces should be provided
#     first_number = int(input("Enter the first number: "))
#     second_number = int(input("Enter the second number: "))
#     total = first_number + second_number
#     return total


"""
 This block of comment is called multi line command
 Used for commands in which precedes more than one line
 into a block of comments
"""
import time


# print(my_function())

# def add(variable_one, variable_two,
#         # extra indentations should be provided to distinguish between arguments and the methods
#         variable_three, variable_four):
#     total = variable_one + variable_two + variable_three + variable_four
#     return total
#
#
# print(add(3, 5, 7, 9))


# def add(
#         variable_one, variable_two,
#         # extra indentations should be provided to distinguish between arguments and the methods
#         variable_three, variable_four):
#     total = variable_one + variable_two + variable_three + variable_four
#     return total
#
#
# print(add(3, 5, 7, 9))

# odd_number = 1
# even_number = 2
#
# if odd_number == 1 and even_number == 2:
#     print("Everything is equal")
#
# total_no_of_days = 20
# total_no_of_sundays = 5
# # operators should be placed before the operands
# total_working_days = (total_no_of_days
#                       - total_no_of_sundays)
#
# print(total_working_days)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)
#
# x = "Python "
# y = "is "
# z = "awesome "
# print(x + y + z)
#
# languages = ["Tamil", "English", "Malayalam"]
# x, y, z = languages
#
# print(x, y, z)
#
# # declaring the scope as global
# first_name = "Dhanesh"
#
#
# def my_fun():
#     print("Welcome " + first_name)
#
#
# my_fun()
#
#
# def my_fun():
#     global first_name  # changing the global variable
#     first_name = "Dinesh" # local variable with the scope within the function
#     print("Welcome " + first_name)
#
#
# my_fun()
#
#
# def my_fun():
#     print("Welcome " + first_name)
#
#
# my_fun()
#
#
# language_list = ["Tamil", "English", "Malayalam"]  # list -> mutable
# language_tuple = ("Tamil", "English", "Malayalam")  # tuple -> immutable , small operation size
# x, y, z = 3, "Harini", 9
# print(id(x))
# # print(y)
# # print(id(y))
# y = "Siva"
# x = 27
# print(id(x))

# print(y)
# print(id(y))

# list_of_users = (["Dhanesh", "dk@123"], ["Harini", "hari@22"], ["Siva", "siva@mo"])
# print(list_of_users)
# list_of_users[2].append("siva@22")
# print(list_of_users)
# list_of_users.
# print(dir(list))
#
# list_of_languages = ['Java', 'Python']
# print(list_of_languages)
# list_of_tools = ['Flyway']
# print(list_of_tools)
# print(list_of_languages.__add__(list_of_tools))
#
# print(list_of_languages)

# import sys
#
#
# class ListExample:
#     grocery_list = ()
#     grocery_list2 = []
#     grocery_list3 = {}
#     grocery = ""
#
#     print(sys.getsizeof(grocery))
#     print(sys.getsizeof(grocery_list))
#     print(sys.getsizeof(grocery_list2))
#     print(sys.getsizeof(grocery_list3))

# print(dir(dict))
# # print(dir(list))
# x = 'Apple'
# X = 'pple'
#
# print(x == X)
# print(x.__contains__(X))
# print(x is X)
# first = {'id': {'name': 'Dhanesh', 'phone_number': '0987654321'}}
# second = {'name': 'Deepak', 'phone_number': '0987654321'}

# print(first.__sizeof__())
# # print(second.__sizeof__())
# # print(first.__eq__(second))
# # print(first.__class__)  # return the class of the data type
# # print(first.__contains__('name'))  # checks if the key is present or not
# # print(first.__class_getitem__(second))
# # print(first.__delitem__('phone_number'))
# print(first.popitem())
# print(first.__format__())
# print(second.__iter__())

# a = {}
# b = []
# c = ()
# # # print(a.__sizeof__())
# print(b.__sizeof__())
# print(c.__sizeof__())

# print('apple' == 'apple')
# a = 'apple'
# b = 'apple'
# print(id(a))
# print(id(id))
# print(a is b)
# print(a is not b)

# is operator & ==

# sample_dic = {1: 'a', 1.05: 'b', 0.5: 'c', (1,): 'd', 2: 'e', 3: 'f' }
# print(sample_dic)
# sample_dic.pop(0.5)
# print(sample_dic)
# print('.get: ', sample_dic.get((1,)))
# print('.items : ', sample_dic.items())
# print('.popitem 1: ', sample_dic.popitem())
# print('.popitem 2: ', sample_dic.popitem())
# print('values: ', sample_dic.values())
#
# sample_list = [1, 2, [3, 4, [5, [6, [7, 8, [9]]], 10, 11]]]
# print(sample_list)
# sample_list[2][2][1][1][2][0] = 10
# print(sample_list)
#
# first_list = [1, 1, 1, 2, 3, 5, 3]
# first_list.remove(1)
# print(first_list)
#
#
# def add(a, b, /, c=4, *, d=4):
#     return a + b + c + d
#
#
# print('Arguents: ', add(3, 4, 1, d=2))

# def decorated_list(function):
#     def decorating_function(list_of_values):
#         return [function(value[0], value[1]) for value in list_of_values]
#
#     return decorating_function
#
#
# @decorated_list
# def add(a, b):
#     return a + b
#
#
# print(add([(1, 2), (3, 4), (5, 6)]))

# def is_even(a):
#     if a % 2 == 0:
#         return a
#
#
# a = range(10)
# for i in a:
#     print(i)
#
# sample_list = [1, 2, 3, 4, 5, 6]
# print('filter: ', list(filter(is_even, sample_list)))
# print('map: ', list(map(is_even, sample_list)))

# sample_list = ['{', '}', '{', '[', ']', '(', ')', '{', '}', '}', '[', '(', ']', ')']
#
#
# def check_count(*list_of_tuples):
#     count = 0
#     for pair in list_of_tuples:
#         if sample_list.count(pair[0]) <= sample_list.count(pair[1]):
#             count += sample_list.count(pair[0])
#         else:
#             count += sample_list.count(pair[1])
#     return count
#
#
# count = check_count(['{', '}'], ['[', ']'], ['(', ')'])
# print('Count: ', count)


# sample_string = '>Al<*97?FY*R:d!vg$v'
# final_string = ''
# counter_string = [x for x in sample_string]
# for count, char in enumerate(counter_string):
#     if 48 <= ord(char) <= 57:
#         counter_string[count] = '0'
#     elif 32 <= ord(char) <= 47:
#         counter_string[count] = '#'
#     elif 65 <= ord(char) <= 98:
#         counter_string[count] = chr(ord(char) + 32)
#     elif 97 <= ord(char) <= 122:
#         counter_string[count] = chr(ord(char) - 32)
#     elif 58 <= ord(char) <= 64:
#         counter_string[count] = '@'
#
# for j in counter_string:
#     final_string += j
# print('result: ', final_string)


# for i in range(rows):
#     if i != rows - 1:
#         print(" " * i + str(rows - i) + (" " * (2 * (rows - 1 - i) - 1) + str(rows - i)))
#     else:
#         print(" " * i + str(rows - i))
# for i in range(1, rows):
#     print(" " * (rows - i - 1) + str(i + 1) + (" " * (2 * i - 1) + str(i + 1)))

# list_of_values = input('Enter the list: ').split(" ")
# for i in list_of_values:
#     print('values: ',i)

