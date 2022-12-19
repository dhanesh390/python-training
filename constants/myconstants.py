# YES = 'yes'
# NO = 'no'
#
# GAME_ATTRIBUTES = ('rock', 'paper', 'scissors')
# TRUE = True
# FALSE = False
#

BANK_ID = 'i2i'
NAME_PATTERN = '[A-Za-z]{2,25}( [A-Za-z]{2,25})?'
CONTACT_PATTERN = '^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$'
DATE_OF_BIRTH_PATTERN = '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$'
AADHAR_PATTERN = '^[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}$'
DATE_TIME_FORMAT = "%d/%m/%Y, %H:%M:%S"

#
# ACCOUNT_ID = 'i2i'

# rows = int(input('No of rows: '))
# for i in range(rows):
#     if i != rows -1:
# k = rows
# for i in range(rows, 0, -1):
#     for j in range(0, rows-i):
#         print(end=" ")
#     for j in range(1, i + 1):
#         print(k, end=' ')
#     k -= 1
#     print()

# print(new_list)


# rows = int(input('No of rows: '))
# new_list = [x for x in range(rows)]
# for i in range(rows):
#     if i != rows - 1:
#         print(" " * i + str(rows - i) + (" " * (2 * (rows - 1 - i) - 1) + str(rows - i)))
#     else:
#         print(" " * i + str(rows - i))
# for i in range(1, rows):
#     print(" " * (rows - i - 1) + str(i + 1) + (" " * (2 * i - 1) + str(i + 1)))
