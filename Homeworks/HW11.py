def do_task_1():
    task = '\nTask 1.\nA person class.\n' \
           'Make a class of called Person. Make the __init__() method take firstname, lastname, and age \n'\
           'as parameters and add them as attributes. \n' \
           'Make another method called talk() which makes prints a greeting from the person containing, \n' \
           'for example like this: \n' \
           '"Hello, my name is Carl Johnson and I\'m 26 years old".\n'

    print(task)

    class Person():
        def __init__(self, firstname, lastname, age):
            self.firstname = firstname
            self.lastname  = lastname
            self.age       = age

        def talk(self):
            print(f'Hello, my name is {self.firstname} {self.lastname} and I\'m {self.age} years old')

    print('Result 1:\n')

    anonym = Person('Ivan', 'Ivanchuk', '24')

    anonym.talk()

def main():
    do_task_1()

    return 0

exit(main())