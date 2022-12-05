from constants import myconstants

# Dictionary comprehension


# list_of_employees = ['Dhanesh', 'Hari', 'Gowtham', 'Deepak', 'Bala']
# list_of_salaries = [2000, 3000, 4000, 5000, 6000]
#
# employees_salary = {employee: salary for employee, salary in zip(list_of_employees, list_of_salaries)}
# print(employees_salary)

no_of_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'friday', 'Saturday', 'Sunday']
hours_of_working = [8, 8, 7, 6, 9, 10, 0]

working_records = {day: hours for day, hours in zip(no_of_days, hours_of_working)}
print('Employee Working Record: ', working_records)

final_records = {day: hours for day, hours in working_records.items() if hours >= 8}
print('Final record: ', final_records)

# ---------------------------------------
# List comprehension..........
list_of_prices = [20, 25, 27, 20, 18]


def get_price_with_tax(price):
    return price + (price * myconstants.TAX)


total_prices = [price + (price * myconstants.TAX) if price >= 20 else price for price in list_of_prices]
# total_prices = [lambda price: price + (price * myconstants.TAX) if price >= 20 else price for price in list_of_prices]

print('Price by list comprehension: ', total_prices)


# Need to use map and filter separately but in comprehension we don't need them
def required_price(price):
    return price >= 20


filtered_price = filter(required_price, list_of_prices)
print('price using filter: ', list(filtered_price))

# final_price = map(lambda price: price + (price * myconstants.TAX), list_of_prices)
final_price = map(get_price_with_tax, list_of_prices)
print('price using map: ', list(final_price))

# list comprehension returns a list & map function returns a object

# Nested list comprehension

# Numbers = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
#
# Result = [Number ** 2 for list in Numbers for Number in list if Number %2 == 0]
#
# print('result is : ', Result)
#  -----------------------------------------



employee_working_records = [[31, 28, 30, 31, 30], [0, 1, 0, 2, 0]]


def calculate_working_days(i, j):
    return j - i


total_working_days = [[calculate_working_days(i[i+1], j) for j in i] for i in employee_working_records]
print(total_working_days)

print(eval(input('Enter equation: ')))


