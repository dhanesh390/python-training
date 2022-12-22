from threading import Thread
from threading import current_thread
from threading import get_ident
from threading import get_native_id
import time

numbers_list = [1, 2, 3, 4, 5]
new_list = []


def _square(numbers, thread_no):
    for i in range(numbers):
        print(f'current thread name: {current_thread().name} current thread id: {get_native_id()} ')
        if thread_no == 1:
            a = numbers_list[i]
            b = a * a
            numbers_list[i] = b
            print(f'\nthread {thread_no} value: {a} :  {b}')
        elif thread_no == 2:
            a = numbers_list[i]
            b = a * a
            new_list.append(b)
            print(f'\nthread {thread_no} value: {a} :  {b}')

        time.sleep(0.1)

    print('1: ', numbers_list)
    print('2: ', new_list)


first_thread = Thread(target=_square, name='threadone', args=(5, 1))

second_thread = Thread(target=_square, name='threadtwo', args=(5, 2))

first_thread.start()
second_thread.start()
first_thread.join()
second_thread.join()

# sample_list = [1, 2, 3, 4]
#
#
# def _cube(numbers):
#     for number in numbers:
#         print(f'\nCurrent thread: {current_thread().name}, thread_id: {get_native_id()}')
#         print(f'\n{number} cube: {number * number * number}')
#         time.sleep(0.1)
#
#
# t1_thread = Thread(target=_cube, args=(sample_list,))
# t2_thread = Thread(target=_cube, args=(sample_list,))
#
# t1_thread.start()
# t2_thread.start()
#
# t1_thread.join()
# t2_thread.join()


