import re
import unittest
from unittest import mock

from Testing import bankmanagement
from bankmanagement import Account
from constants import myconstants
from exception import exceptionhandling
from datetime import datetime, date
from unittest.mock import Mock, patch
import mock_values

account_records = {'i2i0': {'_Account__account_id': 'i2i0', '_Account__name': 'Dhanesh',
                            '_Account__contact_number': '8489335530', '_Account__aadhar_number': '9030 5015 9729',
                            '_Account__age': 22, '_Account__account_balance': 10000.0,
                            '_Account__creation_date': '20/12/2022, 10:54:06',
                            '_Account__updated_date': '20/12/2022, 10:54:06', 'status': True}}


# '_Account__account_balance'


def generate_account_id():
    """ It returns a generated id for each account whenever required"""
    is_continue = True
    count = 0
    while is_continue:
        account_id = 'i2i' + str(count)
        yield account_id
        count += 1


ids = generate_account_id()


def mock_get_account_number():
    return 'i2i0'


def mock_get_account_balance():
    return 10000


def mock_check_account_isavailable(account_id):
    return True


class TestFunction(unittest.TestCase):

    def __init__(self, method_name: str = ...):
        super().__init__(method_name)
        self.account_balance = None
        self.contact_number = None
        self.name = None

    def setUp(self):
        self.account = Account()

    def test_1_set_name(self):
        """ Setter method for name attribute"""
        actual_name = mock_values.name
        second_name = mock_values.second_name
        expected_name = 'Dhanesh'
        self.assertEqual(actual_name, expected_name)
        self.assertRegex(actual_name, myconstants.NAME_PATTERN)
        self.assertIsNot(actual_name, second_name)

    def test_2_get_name(self):
        """ Returns the name attribute value"""
        self.assertIsNotNone(self.account.get_name)
        return self.name

    def test_3_set_contact_number(self):
        """ Setter method for attribute contact number"""
        contact_number = mock_values.contact_number
        expected_value = '8489335530'
        self.assertEqual(contact_number, expected_value)
        self.assertCountEqual(contact_number, expected_value)

    def test_4_get_contact_number(self):
        """ returns the attribute contact number"""
        self.assertIsNotNone(self.account.get_contact_number)
        return self.contact_number

    def test_5_set_name(self):
        """ Setter method for name attribute"""
        actual_name = mock_values.second_name
        expected_name = 'Dhanesh'
        self.assertEqual(actual_name, expected_name)
        self.assertRegex(actual_name, myconstants.NAME_PATTERN)

    def test_6_get_name(self):
        """ Returns the name attribute value"""
        self.assertIsNone(self.account.get_name)
        return self.name

    @patch('builtins.input', return_value=1000)
    # @mock.patch.object(bankmanagement.Account, 'get_account_balance')
    def test_7_withdraw_amount(self, mock_acc_bal):
        bankmanagement.get_account_number = mock_get_account_number
        mock_acc_bal.return_value = account_records[mock_get_account_number()]['_Account__account_balance']

        bankmanagement.check_account_isavailable = Mock(return_value=True)

        bankmanagement.account_records[mock_get_account_number()] = account_records[mock_get_account_number()]

        bankmanagement.get_account_balance = mock_get_account_balance

        response_value = bankmanagement.withdraw_amount()
        print('1: ', response_value)
        self.assertEqual(response_value['_Account__account_balance'], 9000)

    # def test_0_create_account(self):
    #
    #     bankmanagement.account_id = mock_get_account_number()
    #     # account_records[account_id] = mock_values.mock_account_object
    #     sample_object = mock_values.mock_object
    #     self.assertEqual(account_records, sample_object)


if __name__ == '__main__':
    unittest.main()
