print('Task 1: The Guessing Game.\n')
print('''Write a program that generates a random number between 1 and 10 and let’s
the user guess what number was generated. The result should be sent back
to the user via a print statement.
''')
print('Result 1:\n')

import random

vComputerNumber = random.randint(1, 10)

vUserNumber = int(input('Guess the integer designed by computer: '))

if vUserNumber == vComputerNumber:
    print('Congratulation. Its realy  {}!'.format(vUserNumber))
else:
    print('Unfortunately, you lost:( It was {}...'.format(vComputerNumber))

print('')
print('Task 2: The birthday greeting program.\n')
print('''Write a program that takes your name as input, and then your age as input
and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”
''')
print('Result 2:\n')

vName = input('Input your name, please: ')
vAge  = int(input('Input your age, please:  ')) + 1

print('\nHello {}, on your next birthday you’ll be {} years!'.format(vName.title(), vAge))

