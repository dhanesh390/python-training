import csv
import re
from exception import exceptionhandling
from datetime import datetime, date
import os
from bankapplicationlogger import logger
from Testing import util
from constants import myconstants

account_records = {}

file_path = os.getcwd()


class Account:
    """ This class contains the attributes of the account object"""

    def __init__(self):
        self.__account_id = None
        self.__name = None
        self.__contact_number = None
        self.__aadhar_number = None
        self.__age = None
        self.__account_balance = None
        self.__creation_date = datetime.utcnow().strftime(myconstants.DATE_TIME_FORMAT)
        self.__updated_date = datetime.utcnow().strftime(myconstants.DATE_TIME_FORMAT)
        self.status = True

    def set_account_id(self, account_id):
        """ This method sets the account id """
        self.__account_id = account_id

    def get_account_id(self):
        """ This method returns the account id"""
        return self.__account_id

    def set_name(self, name):
        """ Setter method for name attribute"""
        self.__name = name

    def get_name(self):
        """ Returns the name attribute value"""
        return self.__name

    def set_contact_number(self, contact_number):
        """ Setter method for attribute contact number"""
        self.__contact_number = contact_number

    def get_contact_number(self):
        """ returns the attribute contact number"""
        return self.__contact_number

    def set_aadhar_number(self, aadhar_number):
        """ Setter method for attribute aadhar number"""
        self.__aadhar_number = aadhar_number

    def get_aadhar_number(self):
        """ This method returns the aadhar number of the account object"""
        return self.__aadhar_number

    def deposit_amount(self, amount: float):
        """ Setter method to deposit amount in the respective account"""
        if 0 < amount < 1000000:
            self.__account_balance = amount
        else:
            logger.warning('Depositing amount should be less than 100000')
            raise exceptionhandling.InvalidInput('Depositing amount should be less than 100000')

    def get_account_balance(self):
        """ Returns the available balance of the account"""
        return self.__account_balance

    def set_date_of_birth(self, date_of_birth):
        """ gets the date of birth and set the age attribute by converting date of birth into age"""
        today: date = date.today()
        if date_of_birth.year > today.year:
            logger.warning('Error occured in date of birth input')
            raise exceptionhandling.InvalidInput('Enter a valid date of birth')
        else:
            difference_in_year: int = today.year - date_of_birth.year
            preceding_count: int = int((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            age = difference_in_year - preceding_count
            self.__age = age
            logger.info('Successfully converted date of birth into age')

    def get_age(self):
        """ Return the age attribute """
        return self.__age

    def get_created_date(self):
        """ This method returns the creation date of the account"""
        return self.__creation_date

    def updated_on(self, updated_time):
        self.__updated_date = updated_time

    def get_updated_date(self):
        """ This method returns the date of account updation"""
        return self.__updated_date

    def is_active(self, status):
        """ This method sets the status of the account"""
        self.status = status


def generate_account_id():
    """ It returns a generated id for each account whenever required"""
    continue_generating_id = True
    count = 0
    while continue_generating_id:
        account_id = myconstants.BANK_ID + str(count)
        yield account_id
        count += 1


ids = generate_account_id()


def get_contact_number():
    contact_number = input('Enter your contact number: ')
    valid_number = ''
    if re.fullmatch(myconstants.CONTACT_PATTERN, contact_number):
        valid_number = contact_number
    else:
        logger.error('Error occured in phone number')
        print('Enter a valid phone number')
        get_contact_number()
    return valid_number


def get_valid_amount():
    amount = float(input('Enter the depositing amount: '))
    valid_amount = 0
    if amount < 0 or amount > 100000:
        logger.error('Invalid value for object amount')
        print(f'Invalid value for amount ')
        get_valid_amount()
    else:
        valid_amount = amount
    return valid_amount


def create_account():
    logger.info('Entered into account creation')
    new_account = Account()
    account_id = next(ids)

    new_account.set_name(name=util.validate_input(input('Enter your name:'), myconstants.NAME_PATTERN,
                                                  'Use only alphabetic characters'))
    new_account.set_contact_number(contact_number=util.validate_input(input('Enter your contact number:'),
                                                                      myconstants.CONTACT_PATTERN,
                                                                      'Enter a valid phone number'))
    new_account.set_aadhar_number(util.validate_input(input('Enter your aadhar number in the (**** **** ****) format:'),
                                                      myconstants.AADHAR_PATTERN,
                                                      'Enter a valid 12 digit aadhar number'))
    date_of_birth = util.validate_input(input("Enter your birth date (dd/mm/yyyy):"), myconstants.DATE_OF_BIRTH_PATTERN,
                                        'Enter a valid date of birth in (dd/mm/yyyy) format')

    birth_date: datetime = datetime.strptime(date_of_birth, "%d/%m/%Y")
    new_account.set_date_of_birth(date_of_birth=birth_date)
    new_account.deposit_amount(amount=get_valid_amount())
    new_account.set_account_id(account_id=account_id)

    account_records[account_id] = new_account
    logger.info('account successfully created')
    return f'Account successfully created'


def create_account_records():
    logger.info('Starting into the account creation function')
    try:
        with open(file_path + '\\bank_account_records.csv', 'w+') as accounts:
            file_headers = ('_Account__account_id', '_Account__name', '_Account__contact_number',
                            '_Account__aadhar_number', '_Account__age', '_Account__account_balance',
                            '_Account__creation_date', '_Account__updated_date', 'status', '')
            file_writer = csv.DictWriter(accounts, fieldnames=file_headers)
            file_writer.writeheader()

            # for key, value in account_records.items():
            #     file_writer.writerow(value.__dict__)
            # record_file = [file_writer.writerow(j.__dict__) for i, j in account_records.items()]
            return f'Account records successfully created {[file_writer.writerow(j.__dict__) for i, j in account_records.items()]}'

    except FileNotFoundError as file_not_found_error:
        logger.warning("File doesn't exist")
        print(f'Exception occured : {file_not_found_error}')
    logger.info('leaving the account creation function')


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
    """
     This method allows the account holder to withdraw amount from his account or if account doesn't exist returns a
     customized message for the user
    """
    account_id = get_account_number()
    logger.info('entering the cash withdraw module')
    if not check_account_isavailable(account_id):
        logger.warning(f"The account for id {account_id} doesn't exist ")
        raise exceptionhandling.InvalidKey(f"The account for id {account_id} doesn't exist ")
    else:
        account = account_records[account_id]
        amount = float(input('Enter the amount you want to withdraw: '))
        available_balance = account.get_account_balance()
        print('2: ', available_balance)
        if available_balance < amount:
            logger.error(f'Insufficient balance, the available balance is {available_balance}')
            return f'Insufficient balance, the available balance is {available_balance}'
        else:
            balance = available_balance - amount
            account.updated_on(updated_time=datetime.utcnow().strftime(myconstants.DATE_TIME_FORMAT))
            account.deposit_amount(balance)
    logger.info('leaving the cash withdraw module')
    return account.__dict__


def get_account_details_by_account_id(account_id):
    """ This method returns the account details for the respective id"""
    if account_id in account_records.keys():
        result = account_records[account_id]
        return result
    else:
        logger.error(f'No Account found for this id {account_id}')
        raise exceptionhandling.DataNotFoundException(f'No Account found for this id {account_id}')


def get_account_details_by_contact_number(contact_number):
    """ This method returns the account records using the account holders contact number"""
    for i, j in account_records.items():
        if contact_number == j.get_contact_number():
            return j.__dict__
        else:
            logger.warning(f'Account records not found for this {contact_number} contact number')
            raise exceptionhandling.DataNotFoundException(f'No record found for this {contact_number} contact number')


def deposit_amount():
    """ This method is to allow the account holder to deposit amount into his account"""
    account_id = get_account_number()
    try:
        account = get_account_details_by_account_id(account_id=account_id)
        amount = float(input('Enter the amount your want to deposit: '))
        account.deposit_amount(amount=account.get_account_balance() + amount)
        account.updated_on(updated_date=datetime.utcnow().strftime(myconstants.DATE_TIME_FORMAT))
        account_records[account_id] = account
        logger.info(f'rupees {amount} is successfully deposited into the account {account.name}')
        return f'rupees {amount} is successfully deposited into the account {account.name}'
    except exceptionhandling.DataNotFoundException as data_no_found_exception:
        logger.warning(f'Exception occured: {data_no_found_exception}')
        return f'No account found for this id: {account_id}'


def delete_account():
    """ This method is used to delete the account records of the respective account id"""
    account_id = get_account_number()
    try:
        account = get_account_details_by_account_id(account_id=account_id)
        if account is not None:
            account.updated_on(updated_date=datetime.utcnow().strftime(myconstants.DATE_TIME_FORMAT))
            account.is_active(status=False)
            logger.info(f'Account of id {account_id} successfully deleted')
            return f'Account of id {account_id} successfully deleted'
    except exceptionhandling.DataNotFoundException as data_no_found_exception:
        logger.warning(f'Exception occured: {data_no_found_exception}')
        return f'No account records found for this id: {account_id}'


def get_your_account_details():
    """ This method return the account details of the users choice"""
    continue_getting_input = True
    while continue_getting_input:
        print('By account_id -> Enter 1\nBy contact_number -> Enter 2\nEnter 3 to exit')
        try:
            user_input = int(input('Enter your choice: '))
        except ValueError as invalid_value:
            logger.warning(f'Error occured; {invalid_value}')
        else:
            match user_input:
                case 1:
                    result = get_account_details_by_account_id(get_account_number())
                    print(result.__dict__)
                case 2:
                    return get_account_details_by_contact_number(get_contact_number())
                case 3:
                    continue_getting_input = False
                case _:
                    print('Invalid input')


def _init_():
    """ This is the application initializer method which provides the operations of the account management"""
    get_input = True
    while get_input:
        print('Enter 1 to create new account\nEnter 2 to view active accounts\nEnter 3 to get account details\nEnter '
              '4 to deposit amount into your account\nEnter 5 to withdraw amount from your account\nEnter 6 to convert '
              'local records to file\nEnter 7 to delete a account\nEnter 8 to exit\nEnter 9 to view all records')

        user_choice = int(input('Enter your choice: '))
        if user_choice < 0 or user_choice > 10:
            raise exceptionhandling.InvalidInput('Provide valid number value')
        match user_choice:
            case 1:
                print(create_account())
                logger.info('Account created')
            case 2:
                logger.info('Display active account')
                print([{i: j.__dict__} if j.status is True else 'No records found' for i, j in
                       account_records.items()])
            case 3:
                logger.info('Getting user account details')
                result = get_your_account_details()
                print(result)
            case 4:
                logger.info('Entering amount deposit module')
                print(deposit_amount())
            case 5:
                logger.info('Entering amount withdraw module')
                print(withdraw_amount())
            case 6:
                logger.info('Creating local records')
                print(create_account_records())
            case 7:
                logger.info('Deleting a active account')
                print(delete_account())
            case 8:
                get_input = False
            case 9:
                logger.info('get all account records')
                print([{i: j.__dict__} for i, j in account_records.items()])
            case _:
                print('Invalid input')


if __name__ == '__main__':
    logger.info('Application has been started')
    is_continue = True
    while is_continue:
        try:
            _init_()
            logger.info('Application started')
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
        finally:
            logger.info('Application closed')
            print('Application close')
