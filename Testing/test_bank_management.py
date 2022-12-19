import re
import unittest
from bankmanagement import Account
from exception import exceptionhandling
from datetime import datetime, date
from unittest.mock import Mock, patch
import mock_values
account_records = {'i2i0': {'account_id': 'i2i0', 'name': 'Dhanesh', 'contact_number': '8489335530', 'age': 22, 'account_balance': 1000.0, 'creation_date': '19/12/2022, 06:11:42', 'updated_date': '19/12/2022, 06:11:42', 'status': True}}


def generate_account_id():
    """ It returns a generated id for each account whenever required"""
    is_continue = True
    count = 0
    while is_continue:
        account_id = 'i2i' + str(count)
        yield account_id
        count += 1


ids = generate_account_id()


class TestFunction(unittest.TestCase):
    account = Account()

    def __init__(self, method_name: str = ...):
        super().__init__(method_name)
        self.account_balance = None
        self.contact_number = None
        self.name = None

    # @patch(Account.set_name)
    # def test_1_set_name(self):
    #     """ Setter method for name attribute"""
    #     name = input('Enter your name: ')
    #     self.assertRaises(Exception, self.account.set_name(name))
    #
    # @patch(Account.get_name)
    # def test_2_get_name(self):
    #     """ Returns the name attribute value"""
    #     self.assertIsNotNone(self.account.get_name)
    #     return self.name
    #
    # def test_3_set_contact_number(self):
    #     """ Setter method for attribute contact number"""
    #     contact_number = input('Enter your number: ')
    #     self.assertRaises(Exception, self.account.set_contact_number(contact_number))
    #
    # def test_4_get_contact_number(self):
    #     """ returns the attribute contact number"""
    #     self.assertIsNotNone(self.account.get_contact_number())
    #     return self.contact_number
    #
    # def test_5_deposit_amount(self):
    #     """ Setter method to deposit amount in the respective account"""
    #     amount = int(input('Enter depositing amount: '))
    #
    #     if 0 < amount < 100000:
    #         print('1: ', type(100000))
    #         print('2: ', type(self.account.deposit_amount(amount)))
    #         self.assertGreaterEqual(100000, self.account.deposit_amount(amount))
    #     else:
    #         raise exceptionhandling.InvalidInput('Depositing amount should be less than 100000')
    #
    # def test_6_get_account_balance(self):
    #     """ Returns the available balance of the account"""
    #     self.assertIsNotNone(self.account.get_account_balance())
    #     return self.account_balance

    #
    # def test_set_date_of_birth(self):
    #     """ gets the date of birth and set the age attribute by converting date of birth into age"""
    #     today: date = date.today()
    #     if date_of_birth.year > today.year:
    #         raise exceptionhandling.InvalidInput('Enter a valid date of birth')
    #     else:
    #         difference_in_year: int = today.year - date_of_birth.year
    #         preceding_count: int = int((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    #         age = difference_in_year - preceding_count
    #         self.age = age

    # def test_get_age(self):
    #     """ Return the age attribute """
    #     return self.age
    #

    # def test_get_account_details(account_id):
    #     if account_id in account_records.keys():
    #         result = account_records[account_id]
    #         return result
    #     else:
    #         return 'No Account found for this id'

    # def test_get_account_number()
    #     """ Common method to get the input account id"""
    #     account_id: str = input('Enter the account id: ')
    #     return account_id

    # def test_get_account_details(self):
    #     Account.get_account_id = Mock(return_value=mock_values.mock_account_object_id)
    #     account_id = Mock.
    #     if account_id in account_records.keys():
    #         result = account_records[account_id]


    # @staticmethod
    # def test_check_account_isavailable(account_id):
    #     if account_id in account_records.keys():
    #         return True
    #     else:
    #         return False

    # def test_withdraw_amount(self):
    #     Account.get_account_number = Mock(return_value='i2i0')
    #     account_id = Account.get_account_number()
    #     Account.check_account_isavailable = Mock(return_value=True)
    #
    #     if not Account.check_account_isavailable(account_id):
    #         raise exceptionhandling.InvalidKey(f"The account for id {account_id} doesn't exist ")
    #     else:
    #         account = account_records[account_id]
    #         amount = float(input('Enter the amount you want to withdraw: '))
    #         Account.get_account_balance = Mock(return_value=100000)
    #         available_balance = account.get_account_balance()
    #         if available_balance < amount:
    #             return f'Insufficient balance, the available balance is {amount}'
    #         else:
    #             balance = available_balance - amount
    #             account.deposit_amount(balance)
    #
    #     return account.__dict__

    def test_0_create_account(self):
        # new_account = Account()
        # name = input('Enter your name: ')
        # if re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name):
        #     new_account.set_name(name)
        # else:
        #     return 'Use only alphabetic characters'
        # contact_number = input('Enter your contact number: ')
        # if re.fullmatch('^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$',
        #                 contact_number):  # ^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$
        #     new_account.set_contact_number(contact_number)  # '^[6-9]\d{9}$'
        # else:
        #     return 'Enter a valid phone number'
        #
        # birth_date_str: str = input("Enter your birth date (dd/mm/yyyy): ")
        # birth_date: datetime = datetime.strptime(birth_date_str, "%d/%m/%Y")
        # new_account.set_date_of_birth(birth_date)
        #
        # amount = float(input('Enter the depositing amount: '))
        # new_account.deposit_amount(amount)

        # account_id = mock_values.mock_account_object_id
        # account_records[account_id] = mock_values.mock_account_object
        sample_object = mock_values.mock_object
        self.assertEqual(account_records, sample_object)
        return f'Account successfully created'


if __name__ == '__main__':
    unittest.main()
