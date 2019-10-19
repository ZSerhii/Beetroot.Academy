vTask_1 =   'Task 1:\n' \
            'Write a Python function that accepts a string and calculate the number of ' \
            'upper case letters and lower case letters. \n' \
            'Sample String : "The quick Brow Fox":\n' \
            ' > No. of Upper case characters :  3\n' \
            ' > No. of Lower case Characters : 12\n'

vTask_2 =   'Task 2:\n' \
            'Write a Python function that takes a list and returns a new list ' \
            'with unique elements of the first list.\n' \
            'Sample List : [1, 2, 3, 3, 3, 3, 4, 5]\n'         \
            'Unique List : [1, 2, 3, 4, 5]\n'

vTask_3 =   'Task 3:\n' \
            'Write a Python program to print the even numbers from a given list.\n' \
            'Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]\n' \
            'Expected Result : [2, 4, 6, 8]\n'

vTask_4 =   'Task 4:\n' \
            'Write a Python function to check whether a string is a pangram or not. \n' \
            'Note : Pangrams are words or sentences containing every letter of the alphabet at least once.\n' \
            'For example : "The quick brown fox jumps over the lazy dog"\n'

# Task 1 ======================================================================

print(vTask_1)

def GetUpperLowerLetters(AString):
    LUpperCount = 0
    LLowerCount = 0

    print('Input string:', AString, '\n')

    for vLetter in AString:
        if vLetter.isupper():
            LUpperCount += 1
        elif vLetter.islower():
            LLowerCount += 1
    
    print(f' > No. of Upper case characters: {LUpperCount}')
    print(f' > No. of Lower case Characters: {LLowerCount}')

print('Result 1:\n')

GetUpperLowerLetters('The quick Brow Fox')

print('')

# Task 2 ======================================================================

print(vTask_2)

def GetUniqueItemsList(AList):
    LResult = []

    for vItem in AList:
        if not vItem in LResult:
            LResult.append(vItem)

    return LResult

print('Result 2:\n')

vList = [1, 2, 3, 3, 3, 3, 4, 5]

print(f'Unique items of list {vList}:', GetUniqueItemsList(vList), '\n')

# Task 3 ======================================================================

print(vTask_3)

def GetEvenNumbersList(AList):
    return [vItem for vItem in AList if vItem % 2 == 0]

print('Result 3:\n')

vList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f'Even numbers of list {vList}:', GetEvenNumbersList(vList), '\n')

# Task 4 ======================================================================

def is_Pangrams(AString):
    LAlphabet = 'abcdefghijklmnopqrstuvwxyz'
    LLetters  = set()

    for vLetter in AString:
        vLetter = str(vLetter).lower()

        if vLetter in LAlphabet:
            LLetters.add(vLetter)

    return len(LAlphabet) == len(LLetters)

print(vTask_4)

print('Result 4:\n')

vString = 'The quick brown fox jumps over the lazy dog'

vResult = is_Pangrams(vString)

vResultStr = ''

if not vResult:
    vResultStr = 'not '

print(f'Sentence "{vString}" is {vResultStr}({vResult}) Pangrams!')

print('\nThat\'s all Folks!')