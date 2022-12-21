import threading
import time

# c = threading.Condition()
# flag = 0  # shared between Thread_A and Thread_B
# val = 20
#
#
# class ThreadA(threading.Thread):
#     def __init__(self, name):
#         threading.Thread.__init__(self)
#         self.name = name
#
#     def run(self):
#         global flag
#         global val
#         while True:
#             c.acquire()
#             if flag == 0:
#                 print(f'thread name: {self.name}')
#                 print(f"A: val=" + str(val))
#                 time.sleep(0.1)
#                 flag = 1
#                 val = 30
#                 c.notify_all()
#             else:
#                 c.wait()
#             c.release()
#
#
# class ThreadB(threading.Thread):
#     def __init__(self, name):
#         threading.Thread.__init__(self)
#         self.name = name
#
#     def run(self):
#         global flag
#         global val
#         while True:
#             c.acquire()
#             if flag == 1:
#                 print("B: val=" + str(val))
#                 time.sleep(0.5)
#                 flag = 0
#                 val = 20
#                 c.notify_all()
#             else:
#                 c.wait()
#             c.release()
#
#
# a = ThreadA("myThread_name_A")
# b = ThreadB("myThread_name_B")
#
# b.start()
# a.start()
#
# a.join()
# b.join()


def _square(numbers):
    for n in numbers:
        print(f'\n{n} : square = {n * n}')
        time.sleep(0.1)


def _cube(numbers):
    for n in numbers:
        print(f'\n{n} : cube = {n * n * n}')
        time.sleep(0.1)


def _add(numbers):
    total = 0
    for n in numbers:
        total += n
        print(f'\n{n}: sum is: {total}')
        time.sleep(0.1)


numbers = [2, 3, 5, 8]
# start = time.time()
# _square(numbers)
# _cube(numbers)
# end = time.time()
#
# print(f'Execution Time: {end - start}')

start = time.time()

square_thread = threading.Thread(target=_square, args=(numbers,))
cube_thread = threading.Thread(target=_cube, args=(numbers,))
add_thread = threading.Thread(group=None, target=_add, name=None, args=(numbers,), kwargs=None, daemon=True)
print('main thread: ', threading.main_thread())
# print(f'\n1: thread name: {square_thread.name} ')
# print(f'\n1: thread native id: {cube_thread.native_id}')
# print(f'\n1: thread alive: {add_thread.is_alive()}')

square_thread.start()
cube_thread.start()
add_thread.start()


# print(f'\n2: thread name: {square_thread.name} ')
# print(f'\n2: thread native id: {cube_thread.native_id}')
# print(f'\n2: thread alive: {add_thread.is_alive()}')


print(f'\n3: thread alive: {add_thread.is_alive()}')

square_thread.join()
cube_thread.join()
add_thread.join()

# print(f'\n4: thread name: {square_thread.name} ')
# print(f'\n4: thread native id: {cube_thread.native_id}')
# print(f'\n4: thread alive: {add_thread.is_alive()}')


end = time.time()

print(f'Execution Time: {end - start}')
