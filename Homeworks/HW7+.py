vTask_1 =   'Task 1. Count.\n' \
            'Define a program called count that has two arguments called sequence and item.\n' \
            'Return the number of times the item occurs in the list.\n' \
            'For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).\n'

vTask_2 = 'Task 2. Remove duplicates.\n' \
          'Write a program remove_duplicates that takes in a list ' \
          'and removes elements of the list that are the same.\n' \
          'For example: remove_duplicates([1,1,2,2]) should return [1,2].\n'

vTask_3 = 'Task 3. Digits sum.\n' \
          'Write a program called digit_sum that takes a positive integer n as input ' \
          'and returns the sum of all that number\'s digits.\n'

vTask_4 = 'Task 4. Factorial.\n' \
          'To calculate the factorial of a non-negative integer x, ' \
          'just multiply all the integers from 1 through x. \n' \
          'For example: 3! is equal to 1*2*3.\n'

import random

print(vTask_1)
print('Result 1:\n')

vInputList = [random.randint(1, 6) for i in range(1, 10)]

vItem = input(f'Select and input item from list {vInputList}: ')

print(f'Number of times the item "{vItem}" occurs in the list "{vInputList}":', vInputList.count(int(vItem)), '\n')

print(vTask_2)
print('Result 2:\n')

vInputList = [random.randint(1, 6) for i in range(1, 10)]

print(f'List {vInputList} without duplicates with set:  ', list(set(vInputList)))

vResultList = []

for vItem in vInputList:
    if vItem not in vResultList:
        vResultList.append(vItem)

print(f'List {vInputList} without duplicates with loops:', vResultList, '\n')

print(vTask_3)
print('Result 3:\n')

vNumber = input(f'Input a positive integer value: ')
vResult = 0

for vSymbol in vNumber:
    vResult += int(vSymbol)

print(f'Sum of all digits in number {vNumber} =', vResult, '\n')

print(vTask_4)
print('Result 4:\n')

vNumber = int(input(f'Input a positive integer value: '))
vResult = 1

for vInt in range(1, vNumber + 1):
    vResult *= vInt

print(f'{vNumber}! =', vResult, '\n')

