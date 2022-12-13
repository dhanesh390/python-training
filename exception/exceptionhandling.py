print(len(dir(locals()['__builtins__'])))
print(dir(locals()['__builtins__']))


class CustomException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'The custom exception for {self.message}'
        else:
            return 'Custom exception is thrown'


CustomException()
