vTask_1 =   'Task 1. A simple function.\n' \
            'Create a simple function called favourite_movie, which takes a string '   \
            'containing the name of your favourite movie. \nThe function should then ' \
            'print "My favourite movie is name".\n'

vTask_2 =   'Task 2. Creating a dictionary.\n' \
            'Create a function called make_country, which takes in a country\'s name and ' \
            'capital as parameters. \nThen create a dictionary from those parameters,  '   \
            'with "name" and "capital" as keys. \nMake the function print out the values ' \
            'of the dictionary to make sure that it works as intended.\n' 
    
vTask_3 =   'Task 3. A simple calculator.\n' \
            'Create a function called make_operation, which takes in a simple '          \
            'arithmetic operator as a first parameter \n(to keep things simple let it '  \
            'only be "+", "-" or "*") and an arbitrary number of arguments (only '       \
            'numbers) as second parameter. \nThen return the sum or product of all the ' \
            'numbers in the arbitrary parameter. \nFor example: \n'              \
            ' - The call make_operation("+", 7, 7, 2) should return 16\n'        \
            ' - The call make_operation("-", 5, 5, -10, -20) should return 30\n' \
            ' - The call make_operation("*", 7, 6) should return 42\n'   

print(vTask_1)

def favourite_movie(AMovieName):
    '''Takes a string containing the name of your favourite movie'''

    print(f'My favourite movie is "{AMovieName}"!\n')
    
print('Result 1:\n')

favourite_movie('Inception')

print(vTask_2)

def make_country(ACountryName, ACountryCapital):
    '''Takes in a country\'s name and capital as parameters.\n
       Rerurn dictionary with "name" and "capital" as keys
       '''

    return {'name': ACountryName, 'capital': ACountryCapital}

def print_country_dict(ACountryDict):
    '''Print make_country\'s function result - dict'''

    print('Country\'s name and it\'s capital:', ACountryDict)

print('Result 2:\n')

print_country_dict(make_country('Ukraine', 'Kyiv'))
print_country_dict(make_country('Sweden ', 'Stockholm‎'))

print()

print(vTask_3)

def make_operation(AOperation, *ANumbers):
    '''Takes in a simple arithmetic operator ("+", "-" or "*") as a first parameter
       and an arbitrary number of arguments (only numbers) as second parameter.\n
       Return the sum or product of all the numbers in the arbitrary parameter
       '''
    if len(ANumbers) == 0:
        print('Not enough parameters!')

        return None

    LResult = None

    for i in ANumbers:
        if LResult == None:
            LResult = i
            continue

        if AOperation == '+':
            LResult += i        
        elif AOperation == '-':
            LResult -= i
        elif AOperation == '*':
            LResult *= i
        elif AOperation == '/':
            LResult /= i

    return LResult

print('Result 3:\n')

print('make_operation("+", 7, 7, 2)        =', make_operation('+', 7, 7, 2))
print('make_operation("-", 5, 5, -10, -20) =', make_operation('-', 5, 5, -10, -20))
print('make_operation("*", 7, 6)           =', make_operation('*', 7, 6))
print('make_operation("/", 24, 2, 4)       =', make_operation('/', 24, 2, 4))

def format_list(AList):
    return ", ".join([str(vItem) for vItem in vList])

print()

vList = [7, 7, 2]

print(f'make_operation("+", {format_list(vList)}) =', make_operation('+', *vList))

vList = [5, 5, -10, -20]

print(f'make_operation("-", {format_list(vList)}) =', make_operation('-', *vList))

vList = [7, 6]

print(f'make_operation("*", {format_list(vList)}) =', make_operation('*', *vList))

vList = [24, 2, 4]

print(f'make_operation("/", {format_list(vList)}) =', make_operation('/', *vList))

print('\nThat\'s all Folks!')