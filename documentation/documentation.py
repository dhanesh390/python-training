# Collection module in pyhton

""" Counter module in python"""

# Need to import counter from collections modules -> from collections import Counter
"""
 -> It returns the number of times/ frequency of the value in the respected input value 
 
   # number_list = [1, 2, 2, 3, 4, 3, 2, 1, 2, 4, 5, 6, 5]
   # c = Counter(number_list)
   # print('1: ', c) 
   
 -> We can update the counter directly by producing separate inputs
 -> We can also access the values using their key, even it the key doesn't exist it doesn't throw an error, 
    instead it provides with the value as 0 
 
   #  c.update({2: 2, 7: 4})
   #  print('2: ', c)
   #  c.update({7: 1, 2: 1})
   #  print('3: ', c)
   #  c.update({8: 2, 2: 1})
   #  print('4: ', c)
   #  print('5: ', c[4])
   #  c.update('Pythoon')
   #  print('6: ', c)
   
 -> If we try accessing a non-exist key in dictionary it will throw a keyerror

"""

""" defaultDict in collections module"""

# Need to import defaultDict from collections module

"""
 It acts similar to the counter, but the major difference is it takes unavailable key and doesn't throws an error
 instead it provides a default value as provided data type
"""
