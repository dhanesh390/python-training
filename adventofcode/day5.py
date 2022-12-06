import re

one = ['R', 'C', 'H']
two = ['F', 'S', 'L', 'H', 'J', 'B']
three = ['Q', 'T', 'J', 'H', 'D', 'M', 'R']
four = ['J', 'B', 'Z', 'H', 'R', 'G', 'S']
five = ['B', 'C', 'D', 'T', 'Z', 'F', 'P', 'R']
six = ['G', 'C', 'H', 'T']
seven = ['L', 'W', 'P', 'B', 'Z', 'V', 'N', 'S']
eight = ['C', 'G', 'Q', 'J', 'R']
nine = ['S', 'F', 'P', 'H', 'R', 'T', 'D', 'L']

sample_dict = {'1': one, '2': two, '3': three, '4': four, '5': five, '6': six, '7': seven, '8': eight, '9': nine}

# is_continue = True
# while is_continue:
#     value = input()
#     if value != 'end':
#         value = value.split(' ')
#         for i in range(int(value[1])):
#             sample_dict[value[5]].insert(0, sample_dict[value[3]][0])
#             sample_dict[value[3]].pop(0)
#     else:
#         is_continue = False
#
# print(one[0], two[0], three[0], four[0], five[0], six[0], seven[0], eight[0], nine[0])

is_continue = True
while is_continue:
    value = input()
    if value != 'end':
        value = value.split(' ')
        for i in range(int(value[1])):
            sample_dict[value[5]].insert(i, sample_dict[value[3]][i])

        for i in range(int(value[1])):
            sample_dict[value[3]].pop(0)
    else:
        is_continue = False

print(one[0], two[0], three[0], four[0], five[0], six[0], seven[0], eight[0], nine[0])