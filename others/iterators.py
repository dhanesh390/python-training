import itertools

first_list = [1, 2, 3, 4, 5, 6]
second_list = (7, 8, 9, 10, 11)
third_list = 'Python'

iter_obj = iter(first_list)

# while True:
#     try:
#         element = next(iter_obj)
#         print(element)
#     except StopIteration:
#         break

# iter product
print('1 product: ', list(itertools.product(first_list, second_list)))

# iter permutation
print('2 permutation: ', tuple(itertools.permutations(first_list)))

# Combination only takes 2 argument ( 1 - iterable, 2- combination sequence)
print('3 combination: ', list(itertools.combinations(first_list, 1)))

# combination with repeated elements as no of times specified
print('4 comb with repl: ', list(itertools.combinations_with_replacement(third_list, 2)))

# itertools counting
# print('5 iter count: ', list(itertools.count(second_list, 1)))

# itertools cycle
# print('6 iter cycle: ', list(itertools.cycle(first_list)))

# itertools repeat
print('7 iter repeat: ', list(itertools.repeat(first_list, 2)))

# itertools accumulate
print('8 iter acum: ', list(itertools.accumulate(third_list)))

# iter chain
print('9 iter chain: ', list(itertools.chain(first_list, second_list)))

# iter compress
print('10 iter compr: ', list(itertools.compress(first_list, [0, 1, 0, 1, 1, 0])))

# iter dropwhile
print('11 iter dropwhile: ', list(itertools.dropwhile(lambda x: x % 2 == 0, [2, 4, 5, 6, 7])))

# iter takewhile
print('12 iter takewhile: ', list(itertools.takewhile(lambda x: x > 0, [2, 3, -1, -2, 3])))

# iter filterfalse
print('13 iter filter false: ', list(itertools.filterfalse(lambda x: x > 0, [2, 3, -1, -2, 3])))

# iter zip_long
print('14 iter zip long: ', list(itertools.zip_longest(first_list, [0, 'a', 'b'])))


# new_list = itertools.product(first_list, second_list)
# print(next(new_list))
# print(next(new_list))
# print(next(new_list))
# print(next(new_list))
# print(next(new_list))
# print(next(new_list))
# print(next(new_list))


# class PowerTwo:
#     """Class to implement an iterator
#     of powers of two"""
#
#     def __init__(self, max=0):
#         self.max = max
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
#
#
# numbers = PowerTwo(3)
#
# # i = iter(numbers)
#
# for i in PowerTwo(5):
#     print(i)


class EvenNumbers:
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num < 10:
            # next_num = self.num
            self.num += 2
            return self.num
        else:
            raise StopIteration


evens = EvenNumbers()
even_iter = iter(evens)

for n in even_iter:
    print(n)
