import datetime
import time
import calendar


def time_decort_func(func):
    def time_func(*args):
        start_time = datetime.datetime.now()
        print('1: ', start_time)
        result = func(*args)
        end_time = datetime.datetime.now()
        print('2: ', end_time)
        total_time = end_time - start_time
        return result, total_time

    return time_func


@time_decort_func
def add(*args):
    sum = 0
    for a, b in args:
        print('3: ', sum)
        sum += (a * b)
    time.sleep(2)
    return sum


print(add((5, 6), (7, 8), (10, 11)))


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
