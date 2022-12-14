from collections import deque
from collections import namedtuple

movie_screening_record = deque(maxlen=2)


def add_movie_records():
    """ This method creates the movie screening record """
    screening_record = namedtuple('Show', ['movie_name', 'screen_no', 'duration'], defaults=['', '', ''])
    movie_name = input('Enter movie name: ')
    screen_no = input('Enter screen no: ')
    duration = input('Enter movie duration: ')
    show = screening_record._make([movie_name, screen_no, duration])
    print('1: ', show)
    movie_screening_record.append(show)
    return


def deque_operations():
    is_continue = True
    while is_continue:
        print('Enter 1 to append left\nEnter 2 to add at back\nEnter 3 to exit')
        choice = int(input('Enter your choice: '))
        match choice:
            case 1:
                movie_screening_record.appendleft(['mm', '2', '3'])
                print(movie_screening_record)
            case 2:
                movie_screening_record.append(['zz', '3', '4'])
                print(movie_screening_record)
            case 3:
                is_continue = False
            case _:
                print('Invalid input')


def _init_():
    is_continue = True
    while is_continue:
        print('Enter 1 to add show details\nEnter 2 to display records\nEnter 3 to exit\nEnter 4 to check deque '
              'operations')
        user_choice = int(input('Enter your choice: '))
        match user_choice:
            case 1:
                add_movie_records()
            case 2:
                print(movie_screening_record)
            case 3:
                is_continue = False
            case 4:
                deque_operations()
            case _:
                print('Invalid input')


if __name__ == '__main__':
    _init_()


# class Deque:
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def addFront(self, item):
#         self.items.append(item)
#
#     def addRear(self, item):
#         self.items.insert(0, item)
#
#     def removeFront(self):
#         return self.items.pop()
#
#     def removeRear(self):
#         return self.items.pop(0)
#
#     def size(self):
#         return len(self.items)
