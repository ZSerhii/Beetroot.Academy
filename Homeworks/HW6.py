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

print('Lesson topics: Fibonacci sequence.\n')
print('''If n > 1 then (n-1)+(n-2) 
If n == 1 then 1 
If n == 0 then 0. 
''')
print('Result Fibonacci sequence:\n')

vFibonacciCount = int(input('Input the number of Fibonacci sequence elements: '))

print('')

vResult   = 0
vPrevious = 0
vCurrent  = 0

vResultList = []

for i in range(vFibonacciCount):
    vResult = vPrevious + vCurrent

    if i < 2:
        vCurrent  = i
        vResult   = i
    else:
        vPrevious = vCurrent
        vCurrent  = vResult

    vResultList.append(vResult)

print('First {} elements of Fibonacci sequence:\n'.format(vFibonacciCount), vResultList, sep='')

print('Lesson topics: Pascal\'s triangle sequence.\n')
print('''Pascal’s triangle sequence, given positive int k, returns a list of k
lists, each representing a floor in the pyramid/triangle. See the following for
rules: https://en.wikipedia.org/wiki/Pascal%27s_triangle 
''')
print('Result Pascal\'s triangle sequence:\n')

vPascalsDepth = int(input('Input the depth of Pascal\'s triangle sequence: '))
vPascalsPrev  = [] 

print('')

for i in range(vPascalsDepth):
    vPascalsLine = [] 
        
    j = 0
    
    while j <= i:        
        if j == 0 or j == i:
            vPascalsLine.append(1)
        else:
            vPascalsLine.append(vPascalsPrev[j - 1] + vPascalsPrev[j])

        j += 1
    
    vPascalsPrev = vPascalsLine.copy()

    print('{}:'.format(i), vPascalsLine)

print('\nThat\'s all Folks!')