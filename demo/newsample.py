import datetime
import time
import calendar


# def time_decort_func(func):
#     def time_func(*args):
#         start_time = datetime.datetime.now()
#         print('1: ', start_time)
#         result = func(*args)
#         end_time = datetime.datetime.now()
#         print('2: ', end_time)
#         total_time = end_time - start_time
#         return result, total_time
#
#     return time_func
#
#
# @time_decort_func
# def add(*args):
#     sum = 0
#     for a, b in args:
#         print('3: ', sum)
#         sum += (a * b)
#     time.sleep(2)
#     return sum
#
#
# print(add((5, 6), (7, 8), (10, 11)))


# def year_gen():
#     month = 1
#     is_continue = True
#     while is_continue:
#         if month < 13:
#             yield calendar.month_name[month]
#             month += 1

def year_gen():
    for i in range(1, 13):
        yield calendar.month_name[i]


month = year_gen()

for _ in range(12):
    print(next(month))


def word_frequency(file_name):
    words = {}
    with open(file_name, 'r') as files:
        for file in files:
            word = file.replace(',', '').replace('.', '').replace('\n', '')
            for i in word.split(' '):
                if i in words:
                    words[i] += 1
                else:
                    words[i] = 1

    max_words = sorted(words.items(), key=lambda item: item[1], reverse=True)[1:2]

    # first = 0
    # second = 0
    # for key, value in words.items():
    #     if value > first:
    #         second = first
    #         first = value
    #     elif second < value < first:
    #         second = value
    # print(f'2: {second} ')

    first_key, first_value = '', 0
    second_key, second_value = '', 0

    for key, value in words.items():
        if value > first_value:
            second_key, second_value = first_key, first_value
            first_key, first_value = key, value
        elif second_value < value < first_value:
            second_key, second_value = key, value

    print(f'2nd {second_key} : {second_value}')
    return f'1: {words}, \n2: {max_words}'


print(word_frequency('samplefile.txt'))


# print('0: ', sorted(words.items(), key=lambda item: item[1], reverse=True)[:])
    # print('0.1: ', sorted(words.items(), key=lambda item: item[1], reverse=True)[::])
    # print('1: ', sorted(words.items(), key=lambda item: item[1], reverse=True)[:3])
    # print('2: ', sorted(words.items(), key=lambda item: item[1], reverse=True)[2:3])
    # print('3: ', sorted(words.items(), key=lambda item: item[1], reverse=True)[-5:-1])
    #
    # sorted_dict = [{key: value} for key, value in words.items() if value == max(words.values())]  # for i in range(2)
    #
    # sort_dict = [ 'fus' if i == 0 else {key: value} for key, value in words.items() for i in range(2) if value == max(words.values())]

    # def second_max_value():
    #     second_max = {}
    #     for key, value in words.items():
    #
    #         for i in range(2):
    #             if i == 0 and value == max(words.values()):
    #                 del words[key]
    #             elif i == 1 and value == max(words.values()):
    #                 second_max.update({key: words[key]})
    #     return second_max