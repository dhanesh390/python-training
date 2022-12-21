from exception import exceptionhandling
from datetime import datetime, date
from sampleproject import logger
from constants import myconstants


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
            logger.error('Depositing amount should be less than 100000')
            raise exceptionhandling.InvalidInput('Depositing amount should be less than 100000')

    def get_account_balance(self):
        """ Returns the available balance of the account"""
        return self.__account_balance

    def set_date_of_birth(self, date_of_birth):
        """ gets the date of birth and set the age attribute by converting date of birth into age"""
        today: date = date.today()
        if date_of_birth.year > today.year:
            logger.error('Error occured in date of birth input')
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

    def get_updated_date(self):
        """ This method returns the date of account updation"""
        return self.__updated_date

    def is_active(self, status):
        """ This method sets the status of the account"""
        self.status = status
