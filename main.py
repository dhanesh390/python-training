from others import config
from datetime import datetime, date
import re


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # print(config.first_variable)
    # print(config.second_variable)
    # print(dir(dict))
    today: date = date.today()
    print(today)
    # current_date = datetime.utcnow().strftime('%Y-%m-%d')
    # print(current_date)
    # line = '$ cd /'
    # cmd = re.search(r'\$ (cd|ls) (.+)', line)
    # if cmd:
    #     print('ok')
    # else:
    #     print('No')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
