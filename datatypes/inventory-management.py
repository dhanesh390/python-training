from constants import myconstants

list_of_items = {}
is_continue = True


def add(list_of_items):
    """ Return the list of add items"""
    item_name = input('Enter the items name: ')
    item_price = int(input('Enter the items price: '))
    item_quantity = int(input('Enter the total quantity: '))
    item_id = myconstants.STORE_ID + item_name[0:2]
    list_of_items[item_id] = [item_name, item_price, item_quantity]

    return list_of_items


def update(list_of_items):
    """ Updates an existing item"""
    item_id = (input('Enter the item Id: '))
    print(list_of_items[item_id])


def view_all(list_of_items):
    """ Returns a list of all items"""
    if not list_of_items:
        return print('No items available')
    else:
        return print(list_of_items)


def delete():
    item_id = input('Enter the item id you want to delete: ')
    list_of_items.pop(item_id)


while is_continue:
    print('Enter 1 to add an item\nEnter 2 to update an item\nEnter 3 to view all items\nEnter 4 to Delete an item')
    user_choice = int(input('Enter your choice of operation: '))
    if user_choice == 1:
        add(list_of_items)
        print(list_of_items)
    elif user_choice == 2:
        update(list_of_items)
    elif user_choice == 3:
        view_all(list_of_items)
    elif user_choice == 4:
        delete()


