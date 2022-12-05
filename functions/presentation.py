# List comprehension

first_list = []

for letter in 'Python':
    first_list.append(letter)

print(f'Result of conventional loop: {first_list} ')

# difference between conventional loop and list comprehension

second_list = [1, 2, 3, 4, 5, 6]

second_list = [value for value in second_list if value % 2 == 0]
print('Result of list comprehension 1: ', second_list)

third_list = [1, 2, 3, 4, 5, 6]
third_list = [value if value % 2 == 0 else 'odd number' for value in third_list]
# third_list = [value if value % 2 == 0 for value in second_list]
print('Result of list comprehension 2: ', third_list)

fourth_list = [1, 2, 3, 4, 5, 6]
fourth_list = [value if value != 2 else 'odd number' for value in fourth_list if value % 2 == 0]
print('Result of list comprehension 3: ', fourth_list)

fifth_list = [1, 2, 3, 4, 5, 6]
fifth_list = [value for value in fifth_list if value % 2 == 0 if value != 2]
print('Result of list comprehension 4: ', fifth_list)

sixth_list = [1, 2, 3, 4, 5, 6]
sixth_list = list(map(lambda value: value, sixth_list))
print('lambda list: ', sixth_list)

seventh_list = [[['Dhanesh', 1], ['Gowtham', 0], ['Deepak', 15]], [['yuvaraj', 21], ['king', 19], ['rithi', 24]]]
seventh_list = [
    (y[0], 'First batch') if 21 <= y[1] <= 31 else (y[0], 'third batch') if 20 >= y[1] >= 10 else (y[0], 'second batch')
    for x in seventh_list for y in x]
print('Nested list comprehension 1: ', seventh_list)

new_list = [1, 2, 3, 4, 5, 6]
new_list = ['1' if number % 3 == 0 else '2' for number in new_list if number % 2 == 0 or number == 3]
print('list comp 1 with filter: ', new_list)

#  Set comprehension

new_list = [1, 2, 3, 4, 5, 6]
new_list = {number-1 if number % 3 == 0 else number for number in new_list if number % 2 == 0 or number == 3}
print('set comp: ', new_list)

# Dictionary comprehension

employees_list = [{'name': 'Dhanesh', 'role': 'Software developer'}, {'name': 'Deepak', 'role': 'Software developer'},
                  {'name': 'Hari', 'role': 'Testing'}]

developers_list = {employee['name']: employee['role'] for employee in employees_list if 'developer' in employee['role']}
print('Dict comp: ', developers_list)

# Generators

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def number_sequence():
    number = 0
    while True:
        yield number
        number += 1


for number in number_sequence():
    if number <= 10:
        even_number = is_even(number)
        if even_number:
            print(f'{number} is even')
        else:
            print(f'{number} is odd')


number_list = [1, 2, 3, 4, 5]

# number_list = [number*2 for number in number_list]
# print('list comp: ', number_list)

number_list = (number * 2 for number in number_list)
print('generator comprehension 1: ', next(number_list))
print('generator comprehension 2: ', next(number_list))
# print('generator comprehension 3: ', next(number_list))
# print('generator comprehension 4: ', next(number_list))
# print('generator comprehension 5: ', next(number_list))
# print('generator comprehension 6: ', next(number_list))

for number in number_list:
    print(f'generated value: ', number)

#  Passing generator comprehension as arguments directly

print('generator as argument: ', sum(number * 2 for number in range(10)))

"""
 Multiple yield's can be used in a function and so. Each yield will process following the previous yield call
 yield will follow up on each other in the order created
"""


def even_numbers(numbers):
    """ yields the even number of the input """
    for num in range(numbers):
        if num % 2 == 0:
            print('even number: ', num)
            yield num


def square(numbers):
    """ Yields the square of the input"""
    for num in numbers:
        print('squared number: ', num ** 2)
        yield num ** 2


print('Sum is: ', sum(square(even_numbers(10))))


global_variable = 10
print('0', global_variable)

# Arguments


def add(a, b, /, c=4, *, d=4):
    return a + b + c + d


print('Arguents: ', add(3, 4, 1, d=2))


def outer():
    """ Outer function of a nested function declaration"""
    # global_variable = 12
    # print('1', global_variable)
    global global_variable  # It reflects the changes that occurs to a global variable
    global_variable = 14
    print('2', global_variable)
    local_variable = 20
    print('3', local_variable)

    def inner():
        """ Inner function of a nested function declaration"""
        # local_variable = 22
        # print('4', local_variable)
        #  It reflects the changes that occurs to the local variable declared inside a fucntion
        nonlocal local_variable
        local_variable = 24
        print('5', local_variable)

    inner()  # calling the inner function
    print('6', local_variable)


outer()  # calling the outer function
print('7', global_variable)