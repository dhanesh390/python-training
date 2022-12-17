import csv
import re
from exception import exceptionhandling
from collections import OrderedDict
from datetime import datetime, date
import os
from bankapplicationlogger import logger

account_records = {}


file_path = os.getcwd()


class Account:
    """ This class contains the attributes of the account object"""

    def __init__(self, account_creation_date=datetime.utcnow().strftime("%d/%m/%Y"),
                 account_updated_date=datetime.utcnow().strftime("%d/%m/%Y")):
        self.account_id = None
        self.name = None
        self.contact_number = None
        self.age = None
        self.account_balance = None
        self.creation_date = account_creation_date
        self.updated_date = account_updated_date

    def set_account_id(self, account_id):
        """ This method sets the account id """
        self.account_id = account_id

    def get_account_id(self):
        """ This method returns the account id"""
        return self.account_id

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
        if 0 < amount < 1000000:
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

    def created_on(self, date_of_creation):
        self.creation_date = date_of_creation

    def get_created_date(self):
        return self.creation_date

    def updated_on(self, updated_date):
        self.updated_date = updated_date

    def get_updated_date(self):
        return self.updated_date


# account_records = {'i2i0': {'account_id': 'i2i0', 'name': 'Dhanesh', 'contact_number': '8489335530', 'age': 22, 'account_balance': 12345.0, 'creation_date': '17/12/2022', 'updated_date': '17/12/2022'}}


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
    account_id = next(ids)

    get_name = True
    while get_name:
        name = input('Enter your name: ')
        if re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name):
            new_account.set_name(name)
            get_name = False
        else:
            print('Use only alphabetic characters')
    get_contact_number = True
    while get_contact_number:
        contact_number = input('Enter your contact number: ')
        if re.fullmatch('^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$',
                        contact_number):  # ^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$
            new_account.set_contact_number(contact_number)  # '^[6-9]\d{9}$'
            get_contact_number = False
        else:
            print('Enter a valid phone number')

    birth_date_str: str = input("Enter your birth date (dd/mm/yyyy): ")
    birth_date: datetime = datetime.strptime(birth_date_str, "%d/%m/%Y")
    new_account.set_date_of_birth(birth_date)

    amount = float(input('Enter the depositing amount: '))
    new_account.deposit_amount(amount)
    new_account.set_account_id(account_id=account_id)

    account_records[account_id] = new_account

    return f'Account successfully created'


def create_account_records():
    try:
        with open(file_path + '\\bank_account_records.csv', 'w+') as accounts:
            file_headers = ('account_id', 'name', 'contact_number', 'age', 'account_balance', 'creation_date','updated_date', '')
            file_writer = csv.DictWriter(accounts, fieldnames=file_headers)
            file_writer.writeheader()

            record_file = [file_writer.writerow(j.__dict__)for i, j in account_records.items()]
            return record_file

    except FileNotFoundError as ex:
        logger.warning("File doesn't exist")
        print(f'Exception occured : {ex}')


def get_account_number():
    """ Common method to get the input account id"""
    account_id: str = input('Enter the account id: ')
    return account_id


def check_account_isavailable(account_id):
    """ Returns true if the account exist or else it returns false"""
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
            return f'Insufficient balance, the available balance is {available_balance}'
        else:
            balance = available_balance - amount
            account.deposit_amount(balance)

    return account.__dict__


def get_account_details(account_id):
    if account_id in account_records.keys():
        result = account_records[account_id]
        return result.__dict__
    else:
        return f'No Account found for this id {account_id}'


# def deposit_amount():
#     account_id = get_account_number()
#     account = get_account_details(account_id=account_id)
#     if account is not None:
#         amount = float(input('Enter the amount your want to deposit: '))
#         account.deposit_amount(amount=account.get_account_balance() + amount)
#         account_records[account_id] = account
#         return f'rupees {amount} is successfully deposited into the account {account.name}'
#     else:
#         raise exceptionhandling.AccountNotFoundException(f'No account found for the {account_id}')

def deposit_amount():
    account_id = get_account_number()
    account = get_account_details(account_id=account_id)
    try:
        amount = float(input('Enter the amount your want to deposit: '))
        account.deposit_amount(amount=account.get_account_balance() + amount)
        account_records[account_id] = account
        return f'rupees {amount} is successfully deposited into the account {account.name}'
    except KeyError as ex:
        logger.warning(f'Exception occured: {ex}')
        return f'No account found for this id: {account_id}'


def _init_():
    get_input = True
    while get_input:
        print('Enter 1 to create new account\nEnter 2 to view accounts\nEnter 3 to get account details\nEnter 4 to '
              'deposit amount into your account\nEnter 5 to withdraw amount from your account\nEnter 6 to convert '
              'local records to file\nEnter 7 to exit')

        user_choice = int(input('Enter your choice: '))
        # if not str(user_choice).isnumeric():
        #     raise exceptionhandling.InvalidInput('Provide valid number value')
        # if not isinstance(user_choice, int):
        #     raise exceptionhandling.InvalidInput('Provide valid number value')
        match user_choice:
            case 1:
                print(create_account())
                logger.info('Account created')
            case 2:
                print([{i: j.__dict__} for i, j in account_records.items()])
            case 3:
                result = get_account_details(get_account_number())
                print(result)
            case 4:
                print(deposit_amount())
            case 5:
                print(withdraw_amount())
            case 6:
                create_account_records()
            case 7:
                get_input = False
            case _:
                print('Invalid input')


if __name__ == '__main__':
    is_continue = True
    while is_continue:
        try:
            _init_()
            is_continue = False
        except ValueError as ex:
            logger.warning(f'Invalid value Exception occured:  {ex} ')
            print(f'Invalid value Exception occured:  {ex} ')
        except exceptionhandling.InvalidInput as ex:
            logger.warning(f'Invalid input Exception occured:  {ex} ')
            print(f'Invalid input Exception occured:  {ex} ')
        except exceptionhandling.InvalidKey as ex:
            logger.warning(f'Invalid key Exception occured:  {ex} ')
            print(f'Invalid key Exception occured:  {ex} ')
        except Exception as ex:
            logger.warning(f'Exception occured:  {ex} ')
            print(f'Exception occured:  {ex} ')
