x = 2

'''
 Bad Practice
'''

if x == 0:
    print('a')
    pass
elif x == 1:
    print('b')
    pass
elif x == 2:
    print('c')
    pass
elif x == 3:
    print('d')
    pass

'''
 Option 1
'''

x_states_text = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd'
}

print(x_states_text[x])
