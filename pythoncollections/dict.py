from collections import Counter
from collections import defaultdict
from collections import OrderedDict

# -> Default dict
sample_list = defaultdict(str)
sample_list['Dhanesh'] = 'Developer'
sample_list['Deepak'] = 'Tester'

print('1: ', sample_list)

print(sample_list['Gowtham'])
print('2: ', sample_list)

sample_list.pop('Deepak')
print('\n3: ', sample_list)

sample_list['Deepak'] = 'Developer'
print('\n4: ', sample_list)

# Ordered dict ->

sample_list = OrderedDict()
sample_list['Dhanesh'] = 'Developer'
sample_list['Deepak'] = 'Tester'
sample_list['Gowtham'] = 'Developer'

print('\n1.1: ', sample_list)

sample_list.move_to_end('Deepak')
print('\n1.2: ', sample_list)

sample_list.move_to_end('Gowtham', last=False)
print('\n1.3: ', sample_list)


def test_counter():
    c = Counter()
    for i in range(10):
        c[i] = 1
    print(c)


test_counter()


def _test_default_dict():
    d = defaultdict(int)
    for i in range(10):
        d[i] = 1
    print(d)


_test_default_dict()