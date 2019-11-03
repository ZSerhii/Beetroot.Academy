QUESTIONS_PATH = 'C:\\Projects\\Beetroot.Academy\\Lessons\\questions.json'

KEY_ID         = 'id'
KEY_TASK       = 'content'
KEY_VERSIONS   = 'choices'
KEY_VERSION    = 'content'
KEY_IS_CORRECT = 'is_correct'

KEY_VERSION_KEY        = 'key'
KEY_VERSION_VALUE      = 'value'
KEY_VERSION_IS_CORRECT = 'is_correct'

KEY_PROGRESS_SUCCESSES = 'successes'
KEY_PROGRESS_MISTAKES  = 'mistakes'
 
from random import randint
from json   import loads

def load_questions():
    with open(QUESTIONS_PATH) as json_questions:
        json_data = json_questions.read()
        questions = loads(json_data)
    
    return questions

def select_question(questions, available_questions):
    question_id = available_questions[randint(0, len(available_questions) - 1)]
    result      = None

    for question in questions:
        if question[KEY_ID] == question_id:
            result = question

            available_questions.remove(question[KEY_ID])
            
            break

    return result

def render_question(question):
    print(question[KEY_TASK], '?\n', sep='')

    print('Possible answers:')
        
    for version in question[KEY_VERSIONS]:
        render_version(version)

    print()

def render_version(version): 
    version = version_item(version)

    print(version[KEY_VERSION_KEY] + ')', version[KEY_VERSION_VALUE])

def render_user_progress(user_progress):
    passed_questions = user_progress[KEY_PROGRESS_SUCCESSES] + user_progress[KEY_PROGRESS_MISTAKES]

    return (f'Questions: {passed_questions}, ' + 
            f'correct answers: {user_progress[KEY_PROGRESS_SUCCESSES]}, ' + 
            f'mistakes: {user_progress[KEY_PROGRESS_MISTAKES]}')

def version_item(version):
    '''Return dict with keys "key", "value" and "is_correct" from list "choices"'''
    item = version[KEY_VERSION].split(':', 1)

    key   = item[0].replace('*', '').lower()
    value = item[1].strip()

    return {'key': key, 'value': value, 'is_correct': version[KEY_IS_CORRECT]}

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

def correct_answer(question, user_answer):
    result = None

    for version in question[KEY_VERSIONS]:
        version = version_item(version)

        if version[KEY_VERSION_KEY] == user_answer and version[KEY_VERSION_IS_CORRECT]:
            result = version          

            break

    return result

def main():
    questions           = load_questions()
    available_questions = [question[KEY_ID] for question in questions]
    user_progress       = {KEY_PROGRESS_SUCCESSES: 0, 
                           KEY_PROGRESS_MISTAKES:  0}

    current_question = select_question(questions, available_questions)
    
    is_repeat = False

    while True:
        render_question(current_question)

        user_answer = get_user_answer()

        if not user_answer:
            break       
        
        if correct_answer(current_question, user_answer):
            print('\nCongratulations!')            

            current_question = select_question(questions, available_questions)

            if not is_repeat:
                user_progress[KEY_PROGRESS_SUCCESSES] += 1

            is_repeat = False
        else:
            if not is_repeat:
                user_progress[KEY_PROGRESS_MISTAKES] += 1    
            
            is_repeat = True            

            print('\nSorry. Let\'s try again!')

        print(f'{render_user_progress(user_progress)}. Questions left: {len(available_questions)}.\n')

    return 0

exit(main())