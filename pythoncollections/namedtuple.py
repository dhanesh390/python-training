import typing
from collections import namedtuple

# class Employee(typing.NamedTuple):
#     first_name: str
#     last_name: str
#     country: str
#     jobs: list
#
#
# andrew = Employee('Andrew', 'Brown', 'US', ['Develoer', 'Manager'])
# print('1: ', andrew)
# employee = andrew._asdict()
#
# print('2: ', employee)
#
# print(f" 3: First Name: {employee['first_name']}, Duties: {employee['jobs']}")
#
#
# alice = Employee(first_name='Alice', last_name='Stevenson', country='UK', jobs=['Product Owner'])
# print('2: ', alice)


# class Employee:
#     COMPANY_NAME = 'ideas2it'
#
#     def __init__(self, first_name, second_name, role):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.role = role
#
#     def __str__(self):
#         return f'Welcome {self.first_name} {self.second_name} to {Employee.COMPANY_NAME}'

Transaction = namedtuple('Transaction', ['sender', 'amount', 'receiver', 'date'], defaults=['', '', '', ''])
# sample_list = [['dhanesh', '200', 'jio', '12-12-2022']]
print(Transaction)
print(Transaction())
first_transaction = Transaction._make(['dhanesh', '200', 'jio', '12-12-2022'])
print(first_transaction)


