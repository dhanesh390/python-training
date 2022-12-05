import random
def star(func):
    def inner(*args, **kwargs):
        print("*" * 10)
        func(*args, **kwargs)
        print("*" * 10)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 10)
        func(*args, **kwargs)
        print("%" * 10)

    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hi, Dhanesh")


def multiply_by_two(method):
    def _multiply_by_two(a, b):
        return method(a, b) * 2

    return _multiply_by_two


@multiply_by_two
def add(a, b):
    return a + b


print('result 1: ', add(1, 5))


def multiply_by(num):
    def _multiply(method):
        def _multiply_method(a, b):
            return method(a, b) * num

        return _multiply_method

    return _multiply


@multiply_by(4)
def add(a, b):
    return a + b


print('result 2: ', add(1, 5))


def trace(fn):
    def wrapper():
        print('\nbegin executing fn:', fn.__name__, '----')
        retval = fn()
        print('-----end fn:', fn.__name__, '\n')
        return retval

    return wrapper


def twice(fn):
    def wrapper():
        fn()
        fn()

    return wrapper


@trace
@twice
def greet():
    print('Hello World')


greet()


def multiply_by(num):
    def _multiply(method):
        def _multiply_method(a, b):
            return method(a, b) * num

        return _multiply_method

    return _multiply


def divide_by(num):
    def _divide(method):
        def _divide_method(a, b):
            return method(a, b) / num

        return _divide_method

    return _divide


def valid_input(func):
    def function_wrap(a, b, c, d):
        if type(a) is not int or type(b) is not int or type(c) is not int or type(d) is not int:
            return 'Every inputs should be integer'
        else:
            result = func(a, b, c, d)
            return result
    return function_wrap


@valid_input
def calculate(a, b, c, d):
    @multiply_by(c)
    @divide_by(d)
    def add(m, n):
        return m + n

    return add(a, b)


print('result 3: ', calculate(4, 1, 3, 4))
# list_1 = [1, 2, 32, 4, 4, 65, 3, 2, 'A', 'D', None, False, True,
#           0, 1, -2, 2, -33, 0.223, 212, 'string']
# for i in range(1, 10):
#     a = random.choice(list_1)
#     b = random.choice(list_1)
#     c = random.choice(list_1)
#     d = random.choice(list_1)
#     print(f'a: {a} b: {b} c: {c} d: {d}')
#     print('result : ', calculate(a, b, c, d))


def outer_func(firstname): # calculate_bill_amount(amount)
    # free variable + inner function is closure
    def inner_func(msg):  # add_c_gst(amount)
        return f'{msg} {firstname}'

    return inner_func


func = outer_func('Dhanesh')

print(func('Hello'))
print(func.__closure__)