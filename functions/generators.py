# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
#
# def number_sequence():
#     number = 0
#     while True:
#         yield number
#         number += 1
#
#
# for number in number_sequence():
#     if number <= 50:
#         even_number = is_even(number)
#         if even_number:
#             print(f'{number} is even')
#         else:
#             print(f'{number} is odd')


# Using close method in generator to stop the iteration
# for number in number_sequence():
#     if number >= 50:
#         number_sequence().close()
#     else:
#         even_number = is_even(number)
#         if even_number:
#             print(f'{number} is even')
#         else:
#             print(f'{number} is odd')

# for number in number_sequence():
#     if number >= 50:
#         number_sequence().throw(ValueError("Not more than 50"))
#     else:
#         even_number = is_even(number)
#         if even_number:
#             print(f'{number} is even')
#         else:
#             print(f'{number} is odd')

# sequence_number = (number for number in range(10))
#
# for number in sequence_number:
#     print(number)
#
#
# def even_numbers(numbers):
#     for num in range(numbers):
#         if num % 2 == 0:
#             print('even number: ', num)
#             yield num
#
#
# def square(numbers):
#     for num in numbers:
#         print('squared number: ', num ** 2)
#         yield num ** 2
#
#
# print('Sum is: ', sum(square(even_numbers(10))))

# numbers = (number for number in range(0, 10, 2))
# print(sum(square(numbers)))

# for number in numbers:
#     print('first call: ', number)
#
# for number in numbers:
#     print('second call: ', number)

# comprehensed_list = [number**3 for number in range(1, 11) if number % 2 == 0]
# print('Comprehensed list: ', comprehensed_list)
#
# comprehensed_generator = (number**3 for number in range(0, 11) if number % 2 == 0)
# print('generator comp: ', comprehensed_generator)
# # print('sum of comp gen: ', sum(comprehensed_generator))
# for number in comprehensed_generator:
#     print(number)
#
# print('generated comp sum: ', sum(number ** 2 for number in range(1, 11) if number % 2 == 0))
#
# new_list = [1, 2, 3, 4, 5, 6]
#
# new_list = set([lambda number: number * 2 for number in new_list if number % 2 == 0])
# print('lambda list comp: ', new_list)
#
# new_list = [1, 2, 3, 4, 5, 6]
# new_list = {'1' if number % 3 == 0 else '2' for number in new_list if number % 2 == 0 or number == 2}
# print('set comp: ', new_list)


# sample_list = [1, 2, 3, 4, 5, 6]
# sample_list_two = enumerate(sample_list, -3)
# print(list(sample_list_two))
#
# first_list = [1, 2, 3, 4]

condition = "do something-kasi"

list_a = condition.split()
final_value = ''
for alphabet in list_a:
    if "-" in alphabet:
        char = alphabet.split("-")
        for element in char:
            if element == char[-1]:
                final_value += element[::-1]
            else:
                final_value += element[::-1] + '-'
    else:
        final_value += alphabet[::-1] + ' '
        print('final: ', final_value)

print(final_value)

# sample = 'Hi123How32Are56You'
# first_string = ''
# second_string = ''
# third_string = ''
# for char in sample:
#
#     if char in pattern:
#         print('first: ', char)
#     else:
#         print('second: ', char)

# for i in range(len(sample)):
#     if sample[i].isalpha():
#         first_string = sample[i] + first_string
#         print('0', sample[i])
#         print('1', first_string)
#
#     else:
#         first_string += sample[i]
#         print('2', first_string)


# print(int(0.1+0.2) == int(0.3))


