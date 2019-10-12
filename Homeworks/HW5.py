print('Task 1: Exclusive common numbers.\n')
print('''Generate 2 lists of length 10 with random integers from 1 to 10, and make
a third list containing the common integers between the 2 initial lists
without any duplicates.
''')
print('Result 1:\n')

from random import randint

v1stList = [randint(1, 10) for i in range(10)]
v2ndList = [randint(1, 10) for i in range(10)]

print('First list: ', v1stList)
print('Second list:', v2ndList)

vResultList = v1stList + v2ndList
vResultList = list(set(vResultList))

print('Result list:', vResultList, 'with', len(vResultList), 'elements!\n')

print('Task 2: Extracting numbers.\n')
print('''Make a list that contains all integers from 1 to 100, then find all
integers from the list that are divisible by 7 but not a multiple of 5 and
store them in a separate list. Finally print the list.  
''')
print('Result 2:')

vBigList = [vInt + 1 for vInt in range(100)]

print('\nList with all integers from 1 to 100:\n', vBigList, '\n', sep='')

vDiv7NotDiv5List = [vElement for vElement in vBigList if vElement%7 == 0 and vElement%5 != 0]

print('Integers from the list that are divisible by 7 but not a multiple of 5:\n', vDiv7NotDiv5List, sep='')