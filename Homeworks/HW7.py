print('Task 1. Dict comprehension exercise.\n')
print('''Make a program that given a whole sentence (a string) will make a dict
containing all unique words as keys and the number of occurrences as values.
''')
print('Result 1:\n')

vSentence = 'Verbs like Put - Put - Put no change'
vDict     = {vKey : vSentence.split().count(vKey) for vKey in vSentence.split()}

print('Input sentence:\n', vSentence, '\n', sep='')
print('Result dict:\n', vDict, sep='')

print('\nTask 2. List comprehension exercise I.\n')
print('''Consider the following list: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Now, make a program (no longer than one line) that makes a new list
containing all the values in a but no even numbers. 
''')
print('Result 2:\n')

vList = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print('Original list:\n', vList, '\n', sep='')
print('Result list:\n', [vItem for vIndex, vItem in enumerate(vList) if vItem % 2 == 1], sep='')

print('\nTask 3. List comprehension exercise II.\n')
print('''Use a list comprehension to make a list containing tuples (i, j) where i
goes from 1 to 10 and j is corresponding i squared. 
''')
print('Result 3:\n')

print('Result list:\n', [(i, i ** 2) for i in range(1, 11)], sep='')

print('\nThat\'s all Folks!')