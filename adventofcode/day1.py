#
# new_list = [x for x in open('C:/Users/lenovo/Documents/Day1.txt')]
# count = 0
# final_list = []
# for i in new_list:
#     if i != '\n':
#         count += int(i)
#     else:
#         final_list.append(count)
#         count = 0
# print(final_list)
# print(sorted(final_list))
# print('first: ', sorted(final_list)[-1])
# print('2nd: ', sorted(final_list)[-3] + sorted(final_list)[-2] + sorted(final_list)[-1])

input_values = input('Enter the input: ')
first_list = input_values.split("  ")
print(first_list)
