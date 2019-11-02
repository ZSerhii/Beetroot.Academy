def do_task_1():
    task = '\nTask 1.\nMake a class structure in python representing people in a school. \n' \
           'Make a base class called Person, a class called Student, and another one called Teacher. \n' \
           'Try to find as many methods and attributes as you can which belong to the different classes, \n' \
           'and keep in mind which are common and which are not. \n' \
           'For example name should be a Person attribute, while salary should only be available to Teacher.\n'

    print(task)

    class Person():

        GENDERS = {
            0: 'Not specified',
            1: 'Male',
            2: 'Female'
        }

        def __init__(self, firstname, lastname, age, gender = 0):
            self.firstname = firstname
            self.lastname  = lastname
            self.age       = age
            self.gender    = gender
        
    class Student(Person):
        count = 0

        def __init__(self, firstname, lastname, age, gender = 0):
            super().__init__(firstname, lastname, age, gender)

            self.year_study   = 1
            self.orphan       = False
            self.half_orphan  = False
            self.large_family = False  
            self.class_head   = False   

            Student.count += 1      

        def __str__(self):
            return (f'Student {self.firstname} {self.lastname}, {self.age} years old, ' + 
                    f'{self.year_study} year of study, benefits: {self.has_benefits()}')

        def completed_year(self):
            self.year_study += 1

        def has_benefits(self):
            return self.orphan or self.half_orphan or self.large_family

    class Teacher(Person):
        count = 0

        def __init__(self, firstname, lastname, age, salary, gender = 0):
            super().__init__(firstname, lastname, age, gender)

            self.salary      = salary
            self.experience  = 0
            self.disciplines = set()
            self.curator     = False

            Teacher.count += 1

        def __str__(self):
            return (f'Teacher {self.firstname} {self.lastname}, {self.age} years old, ' + 
                    f'{self.experience} years experience, salary: {self.salary}')

        def completed_year(self):
            self.experience += 1

        def add_disciplines(self, discipline):
            self.disciplines.add(discipline)

    print('Result 1:\n')

    student_1 = Student('Ivan',  'Ivanchuk', 6)
    student_2 = Student('Petro', 'Petruk',   7)

    teacher_1 = Teacher('Pavlo', 'Pavlenko',   36, 4000)
    teacher_2 = Teacher('Taras', 'Tarasovych', 47, 6000)

    print(student_1)
    print(student_2)
    print()
    print(teacher_1)
    print(teacher_2)

    student_1.orphan = True
    student_2.completed_year()

    teacher_1.add_disciplines('mathematics')
    teacher_2.experience = 20

    print(student_1)
    print(student_2)
    print()
    print(teacher_1)
    print(teacher_2)

    print(f'{teacher_1.firstname} {teacher_1.lastname} add_disciplines:', teacher_1.disciplines)
    print(f'{teacher_2.firstname} {teacher_2.lastname} add_disciplines:', teacher_2.disciplines)

def main():
    do_task_1()

    return 0

exit(main())