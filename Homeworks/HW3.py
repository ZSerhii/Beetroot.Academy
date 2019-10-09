print('Task 1: The valid phone number program.\n')
print('''Make a program that checks if a string is on the right format for a phone
number. The program should check that the string contains only numerical
characters and is only 10 characters long. Print a suitable message depending
on the outcome of the string evaluation.\n''')

print('Result 1:\n')

vPhone = input('Input the phone number: ').strip()

if vPhone.isnumeric() and len(vPhone) == 10:
    print('Thank you!\n')
else:
    print('Invalid format!')
    print('A phone number can contains only numerical characters and is only 10 characters long\n')

print('Task 2: The math quiz program.\n')
print('''Write a program that asks the answer for a mathematical expression, checks
whether the user is right or wrong, and then responds with a message
accordingly.\n''')

print('Result 2:\n')

vInput = 'Input result for {} = '

vWrongAnswer = '''\nIt's a pity but it's the wrong answer!
Correct answer is {} = {}
Good luck next time. Don't give up!\n'''

vCorrectAnswer = '\nGreat!!! This is the correct answer!\n'

vOperation = '2 + 2'
vAnswer    = input(vInput.format(vOperation)).strip()

if float(vAnswer) != (2 + 2):
    print(vWrongAnswer.format(vOperation, 2 + 2))
else:
    print(vCorrectAnswer)

vOperation = '2 * 2'
vAnswer    = input(vInput.format(vOperation)).strip()

if float(vAnswer) != (2 * 2):
    print(vWrongAnswer.format(vOperation, 2 * 2))
else:
    print(vCorrectAnswer)

vOperation = '2 + (2 * 2)'
vAnswer    = input(vInput.format(vOperation)).strip()

if float(vAnswer) != (2 + (2 * 2)):
    print(vWrongAnswer.format(vOperation, 2 + (2 * 2)))
else:
    print(vCorrectAnswer)

print('')
print('Task 3: The name check.\n')
print('''Write a program that has a variable with your name stored (in lowercase) and
then asks for your name as input. The program should check if your input is
equal to the stored name even if the given name has another case, e.g., if your
input is “Anton” and the stored name is “anton” it should return True. \n''')

print('Result 3:\n')

vName  = 'serhii'
vInput = input('Input your name: ').strip()

if vInput.lower() == vName.lower():
    print('Good morning, {}'.format(vName.title()))
else:
    print("Unfortunately, I don't know you, {}. Goodbye!".format(vInput.title()))