def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y=2):
    return x % y


def is_even(*x):
    return x % 2 == 0


def __init__():
    is_continue = True
    while is_continue:
        print('Choice of operation\n1 to add\n2 to subtract\n3 to multiply\n4 to divide')
        user_choice = int(input('Enter your choice of operation: '))
        a = int(input('Enter the first number: '))
        b = int(input('Enter the second number: '))
        match user_choice:
            case 1:
                print(add(a, b))
            case 2:
                print(subtract(y=a, x=b))
            case 3:
                print(multiply(a, b))
            case 4:
                print(divide(a, b))
            case _:
                print('Invalid input')


if __name__ == '__main__':
    __init__()
