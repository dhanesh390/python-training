# @staticmethod
#     def get_account_number():
#         """ Common method to get the input account id"""
#         account_id: str = input('Enter the account id: ')
#         return account_id
#
#     @staticmethod
#     def get_account_details(account_id):
#         if account_id in account_records.keys():
#             result = account_records[account_id]
#             return result
#         else:
#             return 'No Account found for this id'
#
#     @staticmethod
#     def check_account_isavailable(account_id):
#         if account_id in account_records.keys():
#             return True
#         else:
#             return False
#
#     @staticmethod
#     def withdraw_amount():
#         account_id = Account.get_account_number()
#         if not Account.check_account_isavailable(account_id):
#             raise exceptionhandling.InvalidKey(f"The account for id {account_id} doesn't exist ")
#         else:
#             account = account_records[account_id]
#             amount = float(input('Enter the amount you want to withdraw: '))
#             available_balance = account.get_account_balance()
#             if available_balance < amount:
#                 return f'Insufficient balance, the available balance is {amount}'
#             else:
#                 balance = available_balance - amount
#                 account.deposit_amount(balance)
#
#         return account.__dict__
#
#     @staticmethod
#     def create_account():
#         new_account = Account()
#         name = input('Enter your name: ')
#         if re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name):
#             new_account.set_name(name)
#         else:
#             return 'Use only alphabetic characters'
#         contact_number = input('Enter your contact number: ')
#         if re.fullmatch('^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$',
#                         contact_number):  # ^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$
#             new_account.set_contact_number(contact_number)  # '^[6-9]\d{9}$'
#         else:
#             return 'Enter a valid phone number'

    # get_contact_number = True
        # while get_contact_number:
        #     contact_number = input('Enter your contact number: ')
        #     if re.fullmatch('^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$',
        #                     contact_number):  # ^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$
        #         new_account.set_contact_number(contact_number)  # '^[6-9]\d{9}$'
        #         get_contact_number = False
        #     else:
        #         print('Enter a valid phone number')
#
#         birth_date_str: str = input("Enter your birth date (dd/mm/yyyy): ")
#         birth_date: datetime = datetime.strptime(birth_date_str, "%d/%m/%Y")
#         new_account.set_date_of_birth(birth_date)
#
#         amount = float(input('Enter the depositing amount: '))
#         new_account.deposit_amount(amount)
#
#         account_id = next(ids)
#         account_records[account_id] = new_account
#         print(new_account.get_account_balance())
#         return f'Account successfully created'


# def get_valid_name():
#     get_name = True
#     valid_name = ''
#     while get_name:
#         name = input('Enter your name: ')
#         if re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name):
#             valid_name = name
#             get_name = False
#         else:
#             print('Use only alphabetic characters')
#     return valid_name


# def get_date_of_birth():
#     logger.info('Entered into get date of birth method')
#     _date: str = input("Enter your birth date (dd/mm/yyyy): ")
#     date_of_brith = ''
#     if re.fullmatch('^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$', _date):
#         logger.info('date of birth value matches the pattern')
#         date_of_brith = _date
#     else:
#         logger.error('Error occured in date of birth')
#         print('Enter a valid date of birth in (dd/mm/yyyy) format')
#         get_date_of_birth()
#     logger.info('leaving the date of birth input function')
#     return date_of_brith
