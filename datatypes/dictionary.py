# first_dictionary = {'first_name': 'Jim', 'age': 23, 'height': 6.0, 'job': 'developer', 'company': 'ideas2it'}
#
# print(first_dictionary)
#
#
# def check_key(x):
#     if x in first_dictionary:
#         return 'yes'
#     else:
#         first_dictionary[x] = first_dictionary.setdefault(x, 0)
#
#
# key = input('Enter the key: ')
# print(f"The key {key} is already present: ", check_key(key))
#
# print(first_dictionary.get('first_name'))
# print(first_dictionary['first_name'])
# second_dictionary = {'age': 22}
#
#
# def update_dictionary():
#     for x in first_dictionary:
#         if x in second_dictionary:
#             first_dictionary[x] = second_dictionary[x]
#
#
# update_dictionary()
# print(first_dictionary)

dictionary_one = {'Dhanesh': 21, 'Bala': 22, 'Hari': 23}
# print(dictionary_one)
# # updating keys in dictionary
# dictionary_one['Siva'] = dictionary_one.pop('Hari')
# print(dictionary_one)
#
#
list_of_keys = ['Dinesh', 'Hari', 'Gowtham']
#
dictionary_two = dict(zip(list_of_keys, dictionary_one.values()))
#
print(dictionary_two)

# print(sorted(dictionary_two.items()))
#
#
# # finding the frequency of occurrence in a list
# List1 = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
#
#
# def count_occurrence(test_list):
#
#     sample_dict = {}
#     for i in test_list:
#         sample_dict[i] = sample_dict.get(i, 0) + 1
#     return sample_dict
#
#
# print(count_occurrence(List1))
# if __name__ == "__main__":
#     print(count_occurrence(List1))
#
# third_dictionary = {}.fromkeys(['Hari', 'Siva', 'justin'], [2, 3, 4])
# print(third_dictionary)
