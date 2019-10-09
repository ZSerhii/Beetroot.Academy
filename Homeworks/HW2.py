cur_day = 'sunday'
my_name = 'Serhii'
greeting = 'Good day {}! {} is a perfect day to learn some python.'

print('Task 1: The greeting program.\n')
print('''Make a program that has your name and the current day of the week stored
as separate variables and then prints a message like this:
Good day <name>! <day> is a perfect day to learn some python.
where <name> and <day> are your predefined variables.\n''')

print('Result 1:\n')
print(greeting.format(my_name, cur_day.title()))

my1stName  = 'Serhii'
myLastName = 'Z'

fullname = my1stName + ' ' + myLastName

print('\nTask 2: Manipulate strings.\n')
print('''Save your first and last name as separate variables, then use string
concatenation to add them together with a white space in between and print
a greeting.\n''')

print('Result 2:\n')

print(greeting.format(fullname, cur_day.title()))
print('My name is {1}, {0} {1}!'.format(my1stName, myLastName))

import math

print('\nTask 3: Using python as a calculator.\n')
print('''Make a program with 2 numbers saved in separate variables a and b Then
print the result for each of the following:  
 - Addition. 
 - Subtraction. 
 - Division. 
 - Multiplikation. 
 - Exponent (Power). 
 - Modulus. 
 - Floor division.\n''')
  
print('Result 3:\n')

print('2 + 2 = ', 2 + 2)
print('2 - 2 = ', 2 - 2)
print('7 / 3 = ', 7 / 3)
print('7 // 3 = ', 7 // 3)
print('7 % 3 = ', 7 % 3)
print('2 * 2 = ', 2 * 2)
print('2 ** 3 = ', 2 ** 3)
print('pow(2, 3) = ', 2 ** 3)
print('abs(2 - 22) = ', abs(2 - 22))
print('floor(-21.32) = ', math.floor(-21.32))
print('floor(221.32) = ', math.floor(221.32))
print('ceil(-21.32) = ', math.ceil(-21.32))
print('ceil(221.32) = ', math.ceil(221.32))