print('''Tasks:

1. Щасливі числа.
   Згенерувати список з 3-х випадкових щасливих чисел
   і перевірити чи введене користувачем число є щасливим

2. Таблиця множення.
   Вивести таблицю множення для введеного числа від 1 до 9.

3. Сума чисел.
   Вивести суму чисел від 1 до введеного користувачем значення.

4. Реверс.
   Вивести своє ім\'я задом наперед.

5. Реверс списку.
   Вивести задом наперед всі імена зі списку імен класу.

6. Поліндром.
   Перевірити чи слово є поліндром 
   (однаково пишеться зліва направо та справа наліво).

7. Послідовність Коллатца.
   Отримати число від користувача і вивести послідовність Коллатца, починаючи з цього числа. 
       
   Послідовність формується за наступними правилами:
   - якщо число парне, то ділимо його 2;
   - якщо число непарне, то множимо на 3 і додаємо 1;
   - якщо число рівне 1 - зупинитися.

8. Щасливий квиток.
   Перевірити чи є квиток щасливим. 
   Щасливим є квиток, у якого сума перших 3-х чисел рівна сумі останніх 3-х.
''')

while True:
    vTask = input('\nSelect task ("q" to exit): ')

    print('')

    if vTask == 'q':
        print('That\'s all Folks!')
        break
    if vTask == '1':
        vUser = int(input('Input your numeric: '))

        print('')

        import random

        vLuckyNumerics = set()

        vLuckyNumerics.add(random.randint(1, 10))
        vLuckyNumerics.add(random.randint(1, 10))
        vLuckyNumerics.add(random.randint(1, 10))

        print(vLuckyNumerics)

        if vUser in vLuckyNumerics:
            print('\nYour numeric is luck!')
        else:
            print('\nSo sad... Don\'t worry!')
    elif vTask == '2':
        vUser = int(input('Input your lucky numeric from 1 to 9: '))

        print('\nProduct table of {}'.format(vUser), '\n')

        for i in range(1, 10):
            print('{} x {} = {}'.format(vUser, i, vUser * i))
    elif vTask == '3':
        vUser   = int(input('Input your lucky numeric: '))

        vResult = 0
        vStart  = 1
        vFinish = vUser

        if vUser < 0:
            vFinish = vStart
            vStart  = vUser
    
        for i in range(vStart, vFinish + 1):
            vResult +=i

        print('\nSum numerics from {} to {} ='.format(vStart, vFinish), vResult)
    elif vTask == '4':
        vName    = 'Serhii'
        vReverse = ''

        for vLetter in vName:
            vReverse = vLetter + vReverse
            
        print('Reversed name (by letter):', vReverse)

        vReverse = ''

        for vIndex, vLetter in enumerate(vName):
            vReverse += vName[-(vIndex + 1)]
    
        print('Reversed name (by index): ', vReverse)
    elif vTask == '5':
        vClassNames = ['Serhii', 'Andrii', 'Sasha', 'Ira', 'Roman', 'Oleg', 'Bohdan', 'Stepan', 'Vasyl']

        for vIndex, vItem in enumerate(vClassNames):
            vReverse = ''

            for vLetter in vItem:
                vReverse = vLetter + vReverse

            vClassNames[vIndex] = vReverse

        print('Reversed class names: ', vClassNames)
    elif vTask == '6':
        vWord   = input('Input your word: ')
        vMiddle = len(vWord) // 2
        vResult = True

        for i in range(vMiddle):
            if vWord[i] != vWord[-i - 1]:
                vResult = False
                break

        if vResult:
            print('\nSuccess. Your word {} is polyindrome'.format(vWord))
        else:
            print('\nFail. {} is not polyindrome'.format(vWord.title()))
    elif vTask == '7':
        vCollatzNum = int(input('Input any numeric: '))

        print('\nCollatz sequence element =', vCollatzNum)

        while vCollatzNum != 1:
            if vCollatzNum % 2 == 0:
                vCollatzNum = vCollatzNum // 2
            else:
                vCollatzNum = vCollatzNum * 3 + 1
        
            print('Collatz sequence element =', vCollatzNum)
    elif vTask == '8':
        vTicket = input('Input your ticket number: ')
        vMiddle = len(vTicket) // 2
        vResult = True

        if vMiddle < 3:
            print('\nNot enough digits!')
        else:
            vIndex = 0
            vLeft  = 0
            vRight = 0

            while vIndex < 3:
                vLeft  += int(vTicket[vIndex])
                vRight += int(vTicket[-vIndex - 1])

                vIndex += 1

            if vLeft == vRight:
                print('\nSuccess. Your ticket {} is lucky'.format(vTicket))
            else:
                print('\nFail. {} is not lucky ticket'.format(vTicket))
    else:
        print('Wrong format! Input number of task or "q" to exit!')
