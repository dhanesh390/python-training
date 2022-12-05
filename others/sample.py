# import random  # Multiple imports should be on separate lines
# import myconstants
#
#
# class BlackJack:
#
#     def __init__(self):  # Method belongs to the class
#         pass
#
#     """ Surround method definitions within the class with one blank line"""
#
#     def first_method(self):
#         return None
#
#
# # Surround function and class with Two blank spaces between them
# def deal_card():
#     """ Returns a random card from the deck"""
#     cards = [
#         11, 1, 2, 3, 4,
#         5, 6, 7, 8, 9,
#         10, 10, 10, 10
#     ]
#     card = random.choice(cards)  # Picks up a random card from the deck
#     return card
#
#
# print(deal_card())
#
#
# def calculate_average(
#         first_number, second_number,  # Should provide four extra white spaces for arguments to differentiate from
#         third_number, fourth_number):
#     first_average = (first_number
#                      + second_number) / 2  # Break the line before the binary operator
#
#     second_average = (third_number
#                       + fourth_number) / 2  # Surround binary operators with equal spaces on both sides
#
#     return (first_average + second_average) / 2
#
#
# average = calculate_average(3, 5, 6, 7)  # Should provide a white space after ','
# print(average)
#
# next_calculation = input('Do you want to proceed to next operation: "Yes" or "No" :').capitalize()
# print(next_calculation)
#
# if next_calculation == myconstants.YES:
#     total = deal_card() * average
#     print(total)
#
# else:
#     print("Completed the calculation")

# x = 'Apple'
# y = 'apple'
#
# print(id(x))
# print(id(y))
# z = [1, 2, 3, 4]
# print('initial list: ', id(z))
# z.append(5)
# print('appended list: ', id(z))


# def generate():
#     # print('id of i: ', id(i))
#     i = 0
#     yield i**2
#
#
# for y in range(3):
#     print('id of y: ', id(y))
#     print(id(generate()))
#     z = generate()
#     next(z)
#     print('z is :', z)
#     print('genrated: ', list(z))
#     print('id of generated y: ', id(z))

# list = [1, 2, 3, 1, 1, 1, 2, 3]
# dic = {}
# for i in list:
#     list.count(i)
#     dic[i] = list.count(i)
# print(dic)
#
# dic = {}
# count = 0
# for i in list:
#     if i in dic and dic[i]:
#         dic[i] += 1
#     else:
#         dic[i] = 1
#
# print(dic)
#
# count = 0
# for i in list:
#     if dic.get(i):
#         dic[i] += 1
#     else:
#         dic[i] = 1
#
# print(dic)

# count = 0
# for i in list:
#     for j in list:
#         if i == j:
#             count += 1
#     dic[i] = count
#
#
# print(dic)


list_of_ids = [1, 2, 3, 4, 5, 6]
list_of_names = ['Dhanesh', 'Gowtham', 'Deepak', 'Siva', 'Hari', 'Dhanesh']
list_of_age = [22, 22, 21, 20, 22, 20]
list_of_keys = ['id', 'name', 'age']

sample_list = zip(list_of_ids, list_of_names, list_of_age)

# first_dictionary = [{'id': values[0], 'name': values[1], 'age': values[2]}for values in sample_list]
# print(list(first_dictionary))


second_dictionary = [{list_of_keys[0]: values[0], list_of_keys[1]: values[1], list_of_keys[2]: values[2]}
                     for keys in list_of_keys for values in sample_list]
print(list(second_dictionary))

# print('a: ', sample_list)
# second_list = []
# for element in sample_list:
#     print('0: ', element)
#     if element == '{' and '}' in sample_list:
#         second_list.append(['{', '}'])
#         sample_list.remove('{')
#         sample_list.remove('}')
#         print('1: ', element)
#         print('a: ', sample_list)
#     elif element == '}' and '{' in sample_list:
#         second_list.append(['{', '}'])
#         sample_list.remove('{')
#         sample_list.remove('}')
#     elif element == '[' and ']' in sample_list:
#         second_list.append(['[', ']'])
#         sample_list.remove('[')
#         sample_list.remove(']')
#         print('2: ', element)
#     elif element == ']' and '[' in sample_list:
#         second_list.append(['[', ']'])
#         sample_list.remove('[')
#         sample_list.remove(']')
#     elif element == ')' and '(' in sample_list:
#         second_list.append(['(', ')'])
#         sample_list.remove('(')
#         sample_list.remove(')')
#     elif element == '(' and ')' in sample_list:
#         second_list.append(['(', ')'])
#         sample_list.remove('(')
#         sample_list.remove(')')
#         print('3: ', element)
#
# print('pre-final: ', sample_list)
# print('final: ', second_list)
# print('no of pairs: ', len(second_list))
