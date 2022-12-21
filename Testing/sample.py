from collections import UserString


# class UpperPrintString(str):
#     def __init__(self, value):
#         super.__init__(value.upper())
#
#     # def __str__(self):
#     #     return self.upper()
#
#
# sample_string = UpperPrintString("Hello, Pythonista!")
#
# print('1: ', sample_string)


# class LowerString(UserString):
#
#     def __init__(self, value):
#         super().__init__(value.lower())
#
#
# second_string = LowerString('PYTHON')
#
# print('2: ', second_string)
#
#
# class LowerString(str):
#     def __new__(cls, value):
#         instance = super().__new__(cls, value.lower())
#         return instance
#
#
# third_string = LowerString('PYTHON')
# print('3: ', third_string)