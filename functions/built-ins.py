#  List comprehension
import timeit

first_list = [0, 1, 2, 3, 4, 5, 6, 7]

second_list = [x for x in first_list if x % 2 == 0]

print(second_list)

#  Dictionary comprehension

states = ['A', 2, 'c']
capitals = ['Chennai', 'Kochi', 'Bangalore']

primary_dictionary = {key: value for (key, value) in zip(states, capitals)}
print(primary_dictionary)
print(primary_dictionary['A'])
print(primary_dictionary.get(2))

secondary_dictionary = {x: x ** 2 for x in first_list}
print(secondary_dictionary)

# Set comprehension
first_set = {0, 1, 2, 3, 4, 5, 6, 7}
second_set = {x for x in first_set if x % 2 != 0}
print(second_set)


#  generator comprehension


def increment():
    x = 1
    while x <= 10:
        yield x
        x += 1


for i in increment():
    print(i)


def calculate(a, b=3):
    return a * b


y = {1, 2, 3}
z = (1, 2, 3)
x = map(calculate, y, z)
print(set(x))

print(calculate(1, 2))
print(calculate(5))


sample_list = [1, 2, 3, 4, 5, 6]


def is_even(b):
    return b % 2 == 0


filtered_list = filter(is_even, sample_list)
mapped_list = map(is_even, sample_list)

print(set(filtered_list))
print(list(mapped_list))

sam_list = list(map(lambda a: a**2, range(10)))
sam_list2 = [a**2 for a in range(10)]
print('sam1', sam_list)
print('sam2', sam_list2)


def percentage(*subjects):
    total = 0
    for i in subjects:
        total = total + i
    avg = total / len(subjects)
    return avg


print(percentage(56, 61, 73).__round__(2))


def percentage(**mark_list):
    percentage_list = {}
    for sub in mark_list:
        percentage_list[sub] = mark_list[sub]
    return percentage_list


print(percentage(math=56, english=61, science=73))
print(type(percentage(math=56, english=61, science=73)))


