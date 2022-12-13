# # Reading an existing file
#
# # fp = open(r'C:/Users/lenovo/Documents/Day1.txt', 'r')
# # # fp = open(r'E:\demos\files\sample.txt', 'r')
# #
# # print(fp.read())
#
# # fp = open(rb'C:/Users/lenovo/Documents/SampleDoc.txt', 'r')
# fp = open('C:/Users/lenovo/Documents/Day1.txt', 'r')
# print('before overriding: ', fp.read())
# # fp.close()
#
# text = 'This text will replace the data of the file which has exposed it to them'
# fp = open('C:/Users/lenovo/Documents/Day1.txt', 'w')
# fp.write(text)
# print('Files has been overridden')
# # print(fp.read())
#
#
# fp = open(r'C:/Users/lenovo/Documents/Day1.txt', 'r')
# print('print after overridden: ', fp.read())
# # absolute file_path / Relative file_path need to check -> os file_path module
#
# #  Seeking the required position
#
# f = open('C:/Users/lenovo/Documents/Day 3.txt', "r")
# f.seek(11)
# print(f'seeking: ', {f.read()})
import os


class Employee:
    """ Employee class contains the attributes belonging to the employee objects"""

    def __init__(self, first_name='', second_name='', employee_id='', contact_number=0):
        self.__date_of_birth = None
        self.first_name = first_name
        self.last_name = second_name
        self.employee_id = employee_id
        self.contact_number = contact_number

    def set_date_of_birth(self, date_of_birth):
        """ Setter method for date of birth of the private variable """
        self.__date_of_birth = date_of_birth

    def get_date_of_birth(self):
        """ Getter method for the date of birth variable"""
        return self.__date_of_birth

    def __str__(self):
        """ returns imformation about the employee object """
        return f'Employee Id: {self.employee_id} is  {self.first_name} {self.last_name} '


file_path = os.getcwd()


# def generate_id():
#     id = 0
#     flag = True
#     while True:


def _init_():
    is_continue = True
    while is_continue:
        print('1: Add a new user to the file\n2: View the users data from file ')
        user_choice = int(input('Enter your choice: '))

        file = open(file_path + '\\Employee Details\\employeedetails.txt', 'a+')
        match user_choice:
            case 1:
                first_name = input('Enter your first name: ')
                last_name = input('Enter your last name: ')
                employee_id = input('Enter employee id: ')
                contact_number = int(input('Enter your contact number: '))
                employee = Employee(first_name=first_name, second_name=last_name, employee_id=employee_id,
                                    contact_number=contact_number)
                employee.set_date_of_birth('03.09.2000')
                file.write(employee.__str__())
                file.close()

            case 2:
                with open(file_path + '\\Employee Details\\employeedetails.txt', 'r') as employee_details:
                    print(employee_details.read())


if __name__ == '__main__':
    _init_()

