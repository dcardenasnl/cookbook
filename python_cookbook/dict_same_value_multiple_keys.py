'''
Option 1
'''

my_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 10,
    'e': 20
}

print('my_dict[c]:', my_dict['c'])


'''
Option 2
'''

my_dict = {}
my_dict = dict.fromkeys(['a', 'c', 'd'], 10)
my_dict.update(dict.fromkeys(['b', 'e'], 20))

print('my_dict[c]:', my_dict['c'])


'''
Option 3
'''


class LazyDict(dict):
    def keylist(self, keys, value):
        for key in keys:
            self[key] = value


my_dict = LazyDict()
my_dict.keylist(('a', 'c', 'd'), 10)
my_dict.keylist(('b', 'e'), 20)

print('my_dict[c]:', my_dict['c'])


'''
Option 4
'''

my_dict = {
    ('a', 'c', 'd'): 10,
    ('b', 'e'): 20,
}

print('my_dict[c]:', my_dict['c'])
