import random

def do_task_1():
    task =  '\nTask 1: \nНаписати функцію, яка друкує усі унікальні значення в словнику.\n' \
            'Приклад вхідних даних:\n' \
            '[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]\n' \
            'P.S. Виведіть унікальні значення з усіх словників в списку.\n'

    print(task)

    def get_unique_values_from_dicts_in_list(a_list):
        result = set()
        
        for item in a_list:  
            for key in item:
                result.add(item.get(key))

        return result

    print('Result 1:\n')

    g_list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

    print(get_unique_values_from_dicts_in_list(g_list))

def do_task_2():
    task =  '\nTask 2: \nНаписати функцію, яка перетворює рядок в словник, де ключ - буква, а значення - її кількість в рядку.\n' \
            'Наприклад, з вхідними даними : "beetrootacademy":\n' \
            'Очікується: {"a": 2, "b": 1, "c": 1, "d": 1, "e": 3, "m": 1, "o": 2, "r": 1, "t": 2, "y": 1}\n'

    print(task)

    def get_letters_count_dict(a_string):
        letters = list(set(a_string))

        letters.sort()

        return {letter : a_string.count(letter) for letter in letters}

    print('Result 2:\n')
    print(get_letters_count_dict('beetrootacademy'))

def do_task_3():
    task =  '\nTask 3: \nРозробити функцію counter(a, b), яка приймає 2 аргументи - цілі невід\'ємні числа a та b,\n' \
            'та повертає число - кількість різних цифр числа b, які містяться у числі а.\n' \
            'Наприклад:\n' \
            ' > counter(12345, 567)     >> 1 \n' \
            ' > counter(1233211, 12128) >> 2 \n' \
            ' > counter(123, 45)        >> 0 \n' \

    print(task)

    def counter(a, b):
        number = set(str(b))
        result = 0

        for digit in number:
            if digit in str(a):
                result += 1

        return result

    print('Result 3:\n')

    print('counter(12345, 567)     >>', counter(12345, 567))
    print('counter(1233211, 12128) >>', counter(1233211, 12128))
    print('counter(123, 45)        >>', counter(123, 45))

def do_task_4():
    task =  '\nTask 4: \nНаписати програму-гру, яка вміє загадувати натуральне число від 1 до 100.\n' \
            'Програма повинна загадати число, та запитувати у користувача правильну відповідь, ' \
            'поки він не відгадає, обмеживши 10 спробами.' \
            'На кожній ітерації писати - "Холодно" (Модуль різниці - більший 15), ' \
            '"Тепло" (Модуль різниці - від 5 до 15), або "Гаряче" (Модуль різниці - менший 5), ' \
            'в залежності від того, на скільки користувач близький до відповіді. \n' \
            'Приклад:\n' \
            '> Відгадай число від 1 до 100:\n' \
            'Число: 50\n' \
            '> Холодно\n' \
            'Число: 25\n' \
            '> Тепло\n' \
            'Число: 30\n' \
            '> Тепло\n' \
            'Число: 35\n' \
            '> Холодно\n' \
            'Число: 20\n' \
            '> Гаряче\n' \
            'Число: 18\n' \
            '> Ви вгадали!\n'

    print(task)

    def get_user_value(a_shots):
        input_text = f'Guess the number in range from 1 to 100 or input "q" to exit (attempts left {a_shots}): '

        result = input(input_text).lower()

        while not result.isdigit():
            if result == 'q':
                break

            result = input(input_text).lower()

        if result == 'q':
            result = -1
        else:
            result = int(result)

        return result

    def get_hint(a_correct_value, a_user_value):
        diff = abs(a_correct_value - a_user_value)

        if diff > 15:
            print('Cold')
        elif diff > 5:
            print('Warm')
        elif diff >= 1:
            print('Hot')
        else:
            print('Correct!')

    def check_answer(a_correct_value, a_user_value):
        result = False

        if a_correct_value == a_user_value:
            print('Correct!')

            result = True
        else:
            get_hint(a_correct_value, a_user_value)

        return result

    print('Result 4:\n')

    correct_value   = random.randint(1, 100)
    number_attempts = 10

    for shot in range(number_attempts):
        user_value = get_user_value(10 - shot)

        if user_value < 0:
            break
        
        if check_answer(correct_value, user_value):
            break

        if shot == number_attempts - 1:
            print(f'You lose :( It was {correct_value}')

def do_task_5():
    task = '\nTask 5:\nWrite a Python function that takes two lists ' \
           'and returns True if they have at least one common member.\n'

    print(task)

    def is_common_element(a_list_1, a_list_2):
        result = False

        for item in a_list_1:
            if item in a_list_2:
                result = True
                break

        return result

    print('Result 5:\n')
    
    list_1 = [random.randint(1, 10) for i in range(10)]
    list_2 = [random.randint(1, 20) for i in range(10)]

    print(f'There is common items in list {list_1} and list {list_2}:', is_common_element(list_1, list_2))

def do_task_6():
    task = '\nTask 6:\nWrite a Python function to shuffle and print a specified list.\n' \
           '[1, 2, 3, 4, 6] -> [3, 2, 4, 5, 1]\n'

    print(task)

    def shuffle_list(a_list):
        result = []

        for index, item in enumerate(a_list):
            if index % 2 == 0:
                result.append(item)
            else:
                result.insert(0, item)

        return result
    
    print('Result 6:\n')

    original_list = [random.randint(1, 10) for i in range(10)]

    print(f'Original list {original_list} and shuffled list:', shuffle_list(original_list))    

def do_task_7():
    task =  '\nTask 7:\nWrite a Python function to get first, second best scores from the list.\n' \
            'List may contain duplicates.\n' \
            'Example: [86,86,85,85,85,83,23,45,84,1,2,0] => should get 86, 85\n'

    print(task)

    def get_two_best_scores(a_scores):
        a_scores = list(set(a_scores))

        a_scores.sort(reverse = True)

        return a_scores[:2]

    print('Result 7:\n')

    scores = [86,86,85,85,85,83,23,45,84,1,2,0]

    print(f'First and second best scores from the list {scores}: ', get_two_best_scores(scores))

def do_task_8():
    task = '\nTask 8:\n{"Student": 10, "student1": 20, "student3": 30}\n' \
           'Get first and second best scores students\n'

    print(task)

    def get_first_and_second_best_scores(a_dict):
        scores = list(set(a_dict.values()))

        scores.sort(reverse = True)

        scores = scores[:2]
        result = []

        for score in scores:
            for key, value in a_dict.items():
                if score == value:
                    result.append(key)

        return result

    print('Result 8:\n')

    scores = {"Student": 10, "student1": 20, "student3": 30}

    print(f'First and second best scores from the dict {scores}: ', get_first_and_second_best_scores(scores))

def do_task_9():
    task = '\nTask 9:\nWrite a Python function to display products with price less or equal ' \
           'form user input products:\n' \
           '{"SMART WATCH": 550, "PHONE" : 1000, "PLAYSTATION": 500, "LAPTOP" : 1550, "MUSIC PLAYER" : 600, "TABLET" : 400}\n'

    print(task)    

    def get_products_with_price_less_equal_value(a_products, a_price):
        result = {}

        for key, value in a_products.items():
            if value <= a_price:
                result[key] = value

        return result

    print('Result 9:\n')

    products = {"SMART WATCH"  : 550, 
                "PHONE"        : 1000, 
                "PLAYSTATION"  : 500, 
                "LAPTOP"       : 1550, 
                "MUSIC PLAYER" : 600, 
                "TABLET"       : 400}

    user_value = float(input('Input price: '))

    print(f'Products with price less or equal {user_value}:', get_products_with_price_less_equal_value(products, user_value))

def main():
    do_task_1()
    do_task_2()
    do_task_3()
    do_task_4()
    do_task_5()
    do_task_6()
    do_task_7()
    do_task_8()
    do_task_9()

main()
exit()