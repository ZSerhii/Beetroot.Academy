def do_task_1():
    task = '\nTask 1. Method overloading.\n' \
           'Create a base class named Animal with a method called talk \n' \
           'and then create two subclasses: Dog and Cat, \n' \
           'and make their own implementation of the method talk be different. \n' \
           'For instance Dog\'s can be to print \'voff voff\', \n' \
           'while Cat\'s can be to print \'meow\'.\n'

    print(task)

    class Animal():
        def talk(self):
            raise NotImplementedError('Subclass must implement abstract method')
    
    class Dog(Animal):
        def talk(self):
            print('Voff voff')

    class Cat(Animal):
        def talk(self):
            print('Meow')
    
    print('Result 1:\n')

    sharik  = Dog()
    murchik = Cat()
    
    sharik.talk()
    murchik.talk()

def main():
    do_task_1()

    return 0

exit(main())