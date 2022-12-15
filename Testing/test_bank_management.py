import unittest
from bankmanagement import Account
from exception import exceptionhandling
from datetime import datetime, date

account_records = {}


class TestFunction(unittest.TestCase):
    account = Account()

    def test_set_name_one(self):
        """ Setter method for name attribute"""
        name = input('Enter your name')
        # self.assertRegex('Dhanesh', '[A-Za-z]{2,25}( [A-Za-z]{2,25})?')
        self.ass
        # self.name = name

    def test_get_name_two(self):
        """ Returns the name attribute value"""
        return self.assertIsNotNone(self.account)
        # return self.name

    def test_set_contact_number_three(self):
        """ Setter method for attribute contact number"""
        # self.assertAlmostEqual(8489335530, 8489335530, 0-9, 'Should be valid mobile number')
        self.assertRegex('8489335530', '^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$')
        # self.contact_number = contact_number

    def test_get_contact_number_four(self):
        """ returns the attribute contact number"""
        return self.assertIsNotNone(self.account)
    #
    # def test_deposit_amount(self):
    #     """ Setter method to deposit amount in the respective account"""
    #     if 0 < amount < 100000:
    #         self.account_balance = amount
    #     else:
    #         raise exceptionhandling.InvalidInput('Depositing amount should be less than 100000')
    #
    # def test_get_account_balance(self):
    #     """ Returns the available balance of the account"""
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
    # @staticmethod
    # def test_get_account_details(account_id):
    #     if account_id in account_records.keys():
    #         result = account_records[account_id]
    #         return result
    #     else:
    #         return 'No Account found for this id'


def test_withdraw_amount():
    account_id = get_account_number()
    if not check_account_isavailable(account_id):
        raise exceptionhandling.InvalidKey(f"The account for id {account_id} doesn't exist ")
    else:
        account = account_records[account_id]
        amount = float(input('Enter the amount you want to withdraw: '))
        available_balance = account.get_account_balance()
        if available_balance < amount:
            return f'Insufficient balance, the available balance is {amount}'
        else:
            balance = available_balance - amount
            account.deposit_amount(balance)

    return account.__dict__


if __name__ == '__main__':
    unittest.main()
