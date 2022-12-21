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
            b = a*a
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


first_thread = Thread(target=_square, args=(5, 1))

second_thread = Thread(target=_square, args=(5, 2))


first_thread.start()
second_thread.start()
first_thread.join()
second_thread.join()
