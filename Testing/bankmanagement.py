import re
from exception import exceptionhandling
from collections import defaultdict
from datetime import datetime, date


class Account:
    """ This class contains the attributes of the account object"""

    def __init__(self, account_creation_date=datetime.utcnow().strftime("%d/%m/%Y")):
        self.age = None
        self.account_balance = None
        self.creation_date = account_creation_date
        self.contact_number = None
        self.name = None

    def set_name(self, name):
        """ Setter method for name attribute"""
        self.name = name

    def get_name(self):
        """ Returns the name attribute value"""
        return self.name

    def set_contact_number(self, contact_number):
        """ Setter method for attribute contact number"""
        self.contact_number = contact_number

    def get_contact_number(self):
        """ returns the attribute contact number"""
        return self.contact_number

    def deposit_amount(self, amount: float):
        """ Setter method to deposit amount in the respective account"""
        if 0 < amount < 100000:
            self.account_balance = amount
        else:
            raise exceptionhandling.InvalidInput('Depositing amount should be less than 100000')

    def get_account_balance(self):
        """ Returns the available balance of the account"""
        return self.account_balance

    def set_date_of_birth(self, date_of_birth):
        """ gets the date of birth and set the age attribute by converting date of birth into age"""
        today: date = date.today()
        if date_of_birth.year > today.year:
            raise exceptionhandling.InvalidInput('Enter a valid date of birth')
        else:
            difference_in_year: int = today.year - date_of_birth.year
            preceding_count: int = int((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            age = difference_in_year - preceding_count
            self.age = age

    def get_age(self):
        """ Return the age attribute """
        return self.age

    @staticmethod
    def get_account_details(account_id):
        if account_id in account_records.keys():
            result = account_records[account_id]
            return result
        else:
            return 'No Account found for this id'


# account_records = defaultdict(Account)

account_records = {}


def generate_account_id():
    """ It returns a generated id for each account whenever required"""
    is_continue = True
    count = 0
    while is_continue:
        account_id = 'i2i' + str(count)
        yield account_id
        count += 1


ids = generate_account_id()


def create_account():
    new_account = Account()
    name = input('Enter your name: ')
    if re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name):
        new_account.set_name(name)
    else:
        return 'Use only alphabetic characters'
    contact_number = input('Enter your contact number: ')
    if re.fullmatch('^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$',
                    contact_number):  # ^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$
        new_account.set_contact_number(contact_number)  # '^[6-9]\d{9}$'
    else:
        return 'Enter a valid phone number'

    birth_date_str: str = input("Enter your birth date (dd/mm/yyyy): ")
    birth_date: datetime = datetime.strptime(birth_date_str, "%d/%m/%Y")
    new_account.set_date_of_birth(birth_date)

    amount = float(input('Enter the depositing amount: '))
    new_account.deposit_amount(amount)

    account_id = next(ids)
    account_records[account_id] = new_account
    return f'Account successfully created'


def get_account_number():
    """ Common method to get the input account id"""
    account_id: str = input('Enter the account id: ')
    return account_id


def check_account_isavailable(account_id):
    if account_id in account_records.keys():
        return True
    else:
        return False


def withdraw_amount():
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


def _init_():
    is_continue = True
    while is_continue:
        print('Enter 1 to create new account\nEnter 2 to view accounts\nEnter 3 to get account details\nEnter 4 to '
              'withdraw amount from your account')

        user_choice = int(input('Enter your choice: '))
        if not isinstance(user_choice, int):
            raise exceptionhandling.InvalidInput('Provide valid number value')
        match user_choice:
            case 1:
                print(create_account())
            case 2:
                print([{i: j.__dict__} for i, j in account_records.items()])
            case 3:
                result = Account.get_account_details(get_account_number())
                print(result.__dict__)
            case 4:
                print(withdraw_amount())
            case _:
                print('Invalid input')


if __name__ == '__main__':
    try:
        _init_()
    except Exception as ex:
        print(f'Exception occured:  {ex} ')
        _init_()
