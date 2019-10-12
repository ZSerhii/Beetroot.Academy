print('Task 1.\n')
print('''Make a program that generates a list that has all squared values of integers
from 1 to 100, i.e., like this: [1, 4, 9, 16, 25, 36, ..., 10000] 
''')
print('Result 1:\n')

vResultList = []

for i in range(1, 101):
    vResultList.append(i * i)

print('Squared values list of integers from 1 to 100:\n', vResultList, '\n', sep='')

print('Task 2.\n')
print('''Make a program that prompts the user to input the name of a car, the program
should save the input in a list and ask for another, and then another,
until the user inputs ‘q’, then the program should stop and the list of
cars that was produced should be printed. 
''')
print('Result 2:\n')

vCarList = []

while True:
    vCarName = input('Input the name of a car or letter "q" to exit: ')

    if vCarName == 'q':
        break

    vCarList.append(vCarName)

print('\nYour car list:\n', vCarList, '\n', sep='')

print('Task 3.\n')
print('''Start of with any list containing at least 10 elements, then print all elements
in reverse order. 
''')
print('Result 3:\n')

import random

vAnyList = [random.randint(1, 10) for i in range(20)]

print('Original list:\n', vAnyList, '\n', sep='')

vResultList = vAnyList.copy()
vResultList.reverse()

print('Reverse version 1:\n', vResultList, '\n', sep='')

vResultList = []

for vIndex in range(1, len(vAnyList) + 1):
    vResultList.append(vAnyList[-vIndex])

print('Reverse version 2:\n', vResultList, '\n', sep='')