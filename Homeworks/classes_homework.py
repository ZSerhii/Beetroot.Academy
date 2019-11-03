#Beetroot python
# task 1
# Create new class SortedList, by extending standard list functionality to keep it sorted 
# on creation, appending new elements, adding another list
# e.g. sorted_list = SortedList([2, 3, 1])
# sorted_list -> [1, 2, 3]
# use following function to test your new class
# test_sorted_list(SortedList) -> 'Congrads!'

def test_sorted_list(s_list_class):
    errors_list = []

    s_list = s_list_class([1, 3, 5, 6, 4, 2])
    expected_list = [1, 2, 3, 4, 5, 6]

    if s_list != expected_list:
        errors_list.append('List not sorted on creation')

    s_list.append(-1)
    expected_list.insert(0, -1)

    if s_list != expected_list:
        errors_list.append('List is not sorted on append')

    s_list += [10, -5]
    if s_list != [-5, -1, 1, 2, 3, 4, 5, 6, 10]:
        errors_list.append('List is not sorted on summation')

    if errors_list:
        print('Please, update SortedList to fix following errors:')
        for err in errors_list: print(err)
    else:
        print('Congrads!')

class SortedList(list):
    def __init__(self, iterable = []):
        super().__init__(iterable)
        self.sort()

    def __add__(self, other):
        super().__add__(other)
        self.sort()

    def __iadd__(self, other):
        super().__iadd__(other)
        self.sort()

        return self

    def append(self, value):
        super().append(value)
        self.sort()

    def extend(self, iterable):
        super().extend(iterable)
        self.sort()

    def insert(self, index, value):
        super().insert(index, value)
        self.sort()

print('Task 1:\n')

test_sorted_list(SortedList)

print()

# task 2
# Create new class NewDict that will provide an empty list as a default value for a non-existing key
# Instead of rising KeyError as a regular dictionary will.  
# Data type like that would let us easily deal with different kind of collections
# Hint: accessing dictionary via square parentness syntax `dictionary[key]` 
# uses __getitem__ magic method
# you will need to find the method for setting dictionary item like `dictionary[key] = val`
# school = NewDict()
# school['students'].extend('Alex', 'Ira', 'Bohdan') # regular dictionary would rise KeyError
# school 
# {'students': ['Alex', 'Ira', 'Bohdan']}
# Check your implementation using `test_new_dictionary(NewDict)`

class NewDict(dict):
    def __getitem__(self, key):
        if not super().get(key):
            super().__setitem__(key, [])
            
        return super().get(key)

def test_new_dictionary(new_dict_class):
    city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), 
                 ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), 
                 ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), 
                 ('GA', 'Atlanta')]

    expected_dict = {'NY': ['Albany', 'Syracuse', 'Buffalo', 'Rochester'],
                     'CA': ['Sacramento', 'Palo Alto'],
                     'GA': ['Atlanta'],
                     'TX': ['Austin', 'Houston', 'Dallas']}

    cities_by_state = new_dict_class()
    for state, city in city_list:
        cities_by_state[state].append(city)

    if cities_by_state != expected_dict:
        print('Sorry, something went wrong. Try again.')
    else:
        print('Updated dictionary works as a charm! Great job!')

print('Task 2:\n')

test_new_dictionary(NewDict)

print()

# task3
# Update the quiz program using classes
# class Questions with `questions_list` attribute, `get_random`, `get_by_id`, methods
# class User with `name`, `password` and `score` attributes 
# class Question with `id`, `choices`, `content`, `correct_choice` attributes
# both `User` and `Questins` classes have `from_file` method to create user object 
# by reading information from json file (list of questions in json file for Question, use questions file you have)
# Connect everything with `run_quiz(question_obj, user_obj)` function
# Feel free to add/modify/change example classes as you wish
# Only requirement is to impelement `from_file` functionality
# And operate with Question class instances inside Questions class   

QUESTIONS_PATH = 'C:\\Projects\\Beetroot.Academy\\Lessons\\questions.json'
USER_FILE      = '{"name": "Sergii", "password": "password"}'

from random import randint
from json   import loads

class Question():
    def __init__(self, question):

        self.id      = question['id']
        self.choices = question['choices']
        self.content = question['content']

        for item in self.choices:
            if item['is_correct']:
                self.correct_choice = item

    def render_question(self):
        print(self.content + '?\n')
        print('Possible answers:')
            
        for version in self.choices:
            self.__render_version(version)

        print()

    def __render_version(self, version): 
        version = self.__version_item(version)

        print(version['key'] + ')', version['value'])
    
    def __version_item(self, version):
        '''Return dict with keys "key", "value" and "is_correct" from list "choices"'''
        item = version['content'].split(':', 1)

        key   = item[0].replace('*', '').lower()
        value = item[1].strip()

        return {'key': key, 'value': value, 'is_correct': version['is_correct']}

    def check_answer(self, user_answer):
        return self.__version_item(self.correct_choice)['key'] == user_answer

class Questions():
    def from_file(self, questions_path):
        with open(questions_path) as json_questions:
            json_data = json_questions.read()
            questions = loads(json_data)

        return questions

    def __init__(self, questions_path):
        self.list        = self.from_file(questions_path)
        self.__available = {question['id'] : 1 for question in self.list}
        self.count       = len(self.list)
        self.passed      = 0

    def get_random(self):
        available = tuple([id for id, status in self.__available.items() if status == 1])

        id = available[randint(0, len(available) - 1)]

        self.__available[id] = 0

        return self.get_by_id(id)
    
    def get_by_id(self, id):
        result = None
        
        for question in self.list:
            if question['id'] == id:
                result = question        
                break    
        
        self.passed =+ 1

        return Question(result)
    
    def has_questions(self):
        return len(self.__available) > 0

class User():
    def from_file(self, user_file):
        # with open(user_file) as json_user_data:
        #     json_data = json_user_data.read()
        #     user_data = loads(json_data)

        user_data = loads(user_file)

        self.name     = user_data['name']
        self.password = user_data['password']

    def __init__(self, user_file):
        self.from_file(user_file)

        self.successes = 0
        self.mistakes  = 0
    
    def score(self):
        return self.successes / (self.successes + self.mistakes)

    def user_progress(self):
        passed_questions = self.successes + self.mistakes

        return (f'Questions: {passed_questions}, ' + 
                f'correct answers: {self.successes}, ' + 
                f'mistakes: {self.mistakes}')

def get_user_answer():
    result = None

    while True:
        user_input = input('Select correct answer and input it\'s key or "q" to exit: ')
        user_input = user_input.strip().lower()
    
        if user_input in {'q', 'й'}:
            result = None
            break
        elif (len(user_input) == 1) and (user_input.isalpha() or user_input in {',', '<'}):
            if user_input in {'а', 'a', 'f'}:
                result = 'а'
            elif user_input in {'б', ',', '<'}:
                result = 'б'
            elif user_input in {'в', 'd', 'b'}:
                result = 'в'
            elif user_input in {'г', 'u'}:
                result = 'г'
            elif user_input in {'д', 'l'}:
                result = 'д'
            else:
                result = user_input
            break
        else:
            print('\nWrong format of answer! Try again!\n')

    return result

def run_quiz(question_obj, user_obj):
    result    = False    
    is_repeat = False

    while True:
        question_obj.render_question()

        user_answer = get_user_answer()

        if not user_answer:
            result = False
            break

        if question_obj.check_answer(user_answer):
            print('\nCongratulations!')            

            if not is_repeat:
                user_obj.successes += 1

            result = True
            break
        else:
            if not is_repeat:
                user_obj.mistakes += 1    
            
            is_repeat = True            

            print('\nSorry. Let\'s try again!')

    return result

def main():
    questions = Questions(QUESTIONS_PATH)
    user      = User(USER_FILE)
    
    print('Let the game begin!\n')

    while questions.has_questions():
        question = questions.get_random()

        if not run_quiz(question, user):
            break

        print(f'Questions left: {questions.count - questions.passed}\n')

    print('User progress:', user.user_progress().lower())

    return 0

print('Task 3: \n')

exit(main())