from constants import myconstants
from datetime import date

list_of_accounts = {}


def generate_id():
    value = 0
    id = myconstants.COMPANY_ID + str(value)
    yield id
    value += 1


def add(list_of_accounts):
    # account_id = generate_id()
    year = date.today()
    name = input('Enter your name: ')
    pan_card_number = input('Enter your pan details: ')
    aadhar_card_number = input('Enter your aadhar details: ')
    primary_number = input('Enter your primary contact number: ')
    secondary_number = input('Enter your secondary contact number: ')
    amount = input('Enter the amount your depositing: ')
    account_id = myconstants.ACCOUNT_ID + name[0:2] + str(year.year % 100)

    list_of_accounts[account_id] = {'name': name,
                                          'pan_and_aadhar_details': (pan_card_number, aadhar_card_number),
                                          'contact_number': [primary_number, secondary_number],
                                          'account_balance': amount,
                                          'transactions': []}

    return list_of_accounts


def update(list_of_accounts):
    account_id = get_account_number()
    if not list_of_accounts.__contains__(account_id):
        print("No account found")
    else:
        print('Enter 1 for name\nEnter 2 for primary contact number\nEnter 3 for secondary contact '
              'number\nEnter 4 to credit amount: ')
        user_choice = int(input('Enter your choice of operation: '))
        if user_choice == 1:
            name = input('Enter your name: ')
            list_of_accounts[account_id]['name'] = name
            return list_of_accounts[account_id]
        elif user_choice == 2:
            primary_number = input('Enter the primary number: ')
            list_of_accounts[account_id]['contact_number'][0] = primary_number
            return list_of_accounts[account_id]
        elif user_choice == 3:
            secondary_number = input('Enter the secondary number: ')
            list_of_accounts[account_id]['contact_number'][1] = secondary_number
            return list_of_accounts[account_id]


def display(list_of_accounts):
    if not list_of_accounts:
        return 'No details available'
    else:
        return list_of_accounts


def display_by_id(list_of_accounts):
    account_id = get_account_number()
    if not list_of_accounts[account_id]:
        return 'No account found'
    else:
        return list_of_accounts[account_id]


def delete(list_of_accounts):
    account_id = input('Enter your account id: ')
    if not list_of_accounts[account_id]:
        return 'No account found'
    else:
        list_of_accounts.__delitem__(account_id)
        return 'Successfully deleted'


def get_account_number():
    account_id = input('Enter account id: ')
    return account_id


def __init__():
    is_continue = False
    while not is_continue:
        print('Enter 1 to add an account\nEnter 2 to update an account\nEnter 3 to view all account\nEnter 4 to '
              'view an account\nEnter 5 to delete an account')
        user_choice = int(input('Enter your choice of operation: '))

        if user_choice == 1:
            print(add(list_of_accounts))
        elif user_choice == 2:
            print(update(list_of_accounts))
        elif user_choice == 3:
            print(display(list_of_accounts))
        elif user_choice == 4:
            print(display_by_id(list_of_accounts))
        elif user_choice == 5:
            print(delete(list_of_accounts))


if __name__ == '__main__':
    __init__()
