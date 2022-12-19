import re
from bankapplicationlogger import logger


def validate_input(value, pattern, msg):
    """
     Validation method checks the input value with the pattern sent and returns the value if patter is a match
     or else provides the user with customized message and get the input again and sends them for validation
    """
    get_input = True
    valid_input = ''
    logger.info('Entered into input validate module')
    while get_input:
        if re.fullmatch(pattern=pattern, string=value):
            valid_input = value
            logger.info('Value validation successfully completed')
            get_input = False
        else:
            logger.error('value validation failed')
            print(f'Invalid input {msg} ')
            value = input('Enter again: ')
    return valid_input
