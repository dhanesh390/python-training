import unittest


class Account:
    def __init__(self):
        self.account_id = 'i2i0'
        self.name = 'Dhanesh'
        self.balance = 2500

    def deposit_amount(self):
        self.balance = 3000

    def withdraw_amount(self):
        self.balance = 2000


class TestSampleFunction(unittest.TestCase):

    def setUp(self):
        self.account = Account()

    def test_deposit_amount(self):
        self.assertIs(self.account.deposit_amount(), 2000)


if __name__ == '__main__':
    unittest.main()