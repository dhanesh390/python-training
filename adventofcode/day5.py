import re

# one = ['R', 'C', 'H']
# two = ['F', 'S', 'L', 'H', 'J', 'B']
# three = ['Q', 'T', 'J', 'H', 'D', 'M', 'R']
# four = ['J', 'B', 'Z', 'H', 'R', 'G', 'S']
# five = ['B', 'C', 'D', 'T', 'Z', 'F', 'P', 'R']
# six = ['G', 'C', 'H', 'T']
# seven = ['L', 'W', 'P', 'B', 'Z', 'V', 'N', 'S']
# eight = ['C', 'G', 'Q', 'J', 'R']
# nine = ['S', 'F', 'P', 'H', 'R', 'T', 'D', 'L']
#
# sample_dict = {'1': one, '2': two, '3': three, '4': four, '5': five, '6': six, '7': seven, '8': eight, '9': nine}

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

# is_continue = True
# while is_continue:
#     value = input()
#     if value != 'end':
#         value = value.split(' ')
#         for i in range(int(value[1])):
#             sample_dict[value[5]].insert(i, sample_dict[value[3]][i])
#
#         for i in range(int(value[1])):
#             sample_dict[value[3]].pop(0)
#     else:
#         is_continue = False
#
# print(one[0], two[0], three[0], four[0], five[0], six[0], seven[0], eight[0], nine[0])

a1 = ['T', 'R', 'G', 'W', 'Q', 'M', 'F', 'P']
b2 = ['R', 'F', 'H']
c3 = ['D', 'S', 'H', 'G', 'V', 'R', 'Z', 'P']
d4 = ['G', 'W', 'F', 'B', 'P', 'H', 'Q']
e5 = ['H', 'J', 'M', 'S', 'P']
f6 = ['L', 'P', 'R', 'S', 'H', 'T', 'Z', 'M']
g7 = ['L', 'M', 'N', 'H', 'T', 'P']
h8 = ['R', 'Q', 'D', 'F']
i9 = ['H', 'P', 'L', 'N', 'C', 'S', 'D']
sample_dict = {'1': a1, '2': b2, '3': c3, '4': d4, '5': e5, '6': f6, '7': g7, '8': h8, '9': i9}

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

print(a1[0], b2[0], c3[0], d4[0], e5[0], f6[0], g7[0], h8[0], i9[0])
