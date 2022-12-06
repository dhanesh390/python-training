import re


# def advent_function_one():
#     count = 0
#     is_continue = True
#     while is_continue:
#         value = input()
#         if value != 'end':
#             value = re.split(',|-', value)
#             if int(value[0]) <= int(value[2]) and int(value[1]) >= int(value[3]):
#                 count += 1
#             elif int(value[0]) >= int(value[2]) and int(value[1]) <= int(value[3]):
#                 count += 1
#         else:
#             is_continue = False
#
#     return count
#
#
# print(advent_function_one())

# def advent_function_two():
#     count = 0
#     is_continue = True
#     while is_continue:
#         value = input()
#         if value != 'end':
#             value = re.split(',|-', value)
#             if int(value[0]) <= int(value[2]) or int(value[1]) >= int(value[3]):
#                 count += 1
#             # elif int(value[0]) >= int(value[2]) or int(value[1]) <= int(value[3]):
#             #     count += 1
#         else:
#             is_continue = False
#
#     return count
#
#
# print(advent_function_two())

def advent_function_two():
    count = 0
    first_set = set()
    second_set = set()
    is_continue = True
    while is_continue:
        value = input()
        if value != 'end':
            value = re.split(',|-', value)
            for i in range(int(value[0]), int(value[1])+1):
                first_set.add(i)
            for j in range(int(value[2]), int(value[3])+1):
                second_set.add(j)

            if len(first_set & second_set) >0:
                count += 1

            first_set = set()
            second_set = set()
        else:
            is_continue = False

    return count


print(advent_function_two())