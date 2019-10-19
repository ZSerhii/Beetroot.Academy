vQuestions = [{'task'   :  '2 + 4 + 18 / 2 =',
               'kind'   :  'select',
               'answers':  [{'version': 16, 'is_correct': False, 'is_show2select': True}, 
                            {'version': 15, 'is_correct':  True, 'is_show2select': True}]},
           
              {'task'   :  '1 + 2 + 3 + 4 =',
               'kind'   :  'select',
               'answers':  [{'version':  1, 'is_correct': False, 'is_show2select': True}, 
                            {'version':  2, 'is_correct':  True, 'is_show2select': True}, 
                            {'version':  3, 'is_correct':  True, 'is_show2select': True}, 
                            {'version':  4, 'is_correct':  True, 'is_show2select': True}, 
                            {'version':  5, 'is_correct':  True, 'is_show2select': True}, 
                            {'version':  6, 'is_correct':  True, 'is_show2select': True}, 
                            {'version':  7, 'is_correct':  True, 'is_show2select': True}, 
                            {'version':  8, 'is_correct':  True, 'is_show2select': True}, 
                            {'version':  9, 'is_correct':  True, 'is_show2select': True}, 
                            {'version': 10, 'is_correct':  True, 'is_show2select': True}]},
           
              {'task'   :  '2 + 2 * 2 =',
               'kind'   :  'input',               
               'answers':  [{'version':       6, 'is_correct': True,  'is_show2select':  True}, 
                            {'version':   'six', 'is_correct': True,  'is_show2select': False}, 
                            {'version':       8, 'is_correct': False, 'is_show2select':  True}, 
                            {'version': 'eight', 'is_correct': False, 'is_show2select': False}]},
          
              {'task'   :  '2 + 8 * 2 / 4 + 1 =',
               'kind'   :  'input',               
               'answers':  [{'version':       7, 'is_correct':  True, 'is_show2select':  True}, 
                            {'version': 'seven', 'is_correct':  True, 'is_show2select': False}, 
                            {'version':       9, 'is_correct': False, 'is_show2select':  True}, 
                            {'version':  'nine', 'is_correct': False, 'is_show2select': False}]}]

KEY_TASK           = 'task'
KEY_KIND           = 'kind'
KEY_ANSWERS        = 'answers'
KEY_VERSION        = 'version'
KEY_IS_CORRECT     = 'is_correct'
KEY_IS_SHOW2SELECT = 'is_show2select'

VALUE_KIND_SELECT = 'select'
VALUE_KIND_INPUT  = 'input'

def select_question(AIndex):
    '''Return a new random value in the range of 0 to the number of questions
       if the input parameter < 0, otherwise does not change it
       '''
    from random import randint

    if AIndex < 0:
        AIndex = randint(0, len(vQuestions) - 1)

    return AIndex

def render_question(AIndex):
    print(vQuestions[AIndex][KEY_TASK], '?\n')

    if vQuestions[AIndex][KEY_KIND] == VALUE_KIND_SELECT: 
        print('Possible answers:')
        
        vPrintIndex = 0

        for vVersion in vQuestions[AIndex][KEY_ANSWERS]:
            if vVersion[KEY_IS_SHOW2SELECT]:
                vPrintIndex += 1
                print(vPrintIndex, ': ', vVersion[KEY_VERSION])

def answer_question(AIndex, AUserAnswer):
    if vQuestions[AIndex][KEY_KIND] == VALUE_KIND_SELECT:
        vVersionIndex = 0

        for vVersion in vQuestions[AIndex][KEY_ANSWERS]:
            if vVersion[KEY_IS_SHOW2SELECT]:
                vVersionIndex += 1

                if vVersionIndex == AUserAnswer:
                    return vVersion[KEY_VERSION]

    elif vQuestions[AIndex][KEY_KIND] == VALUE_KIND_INPUT:   
        for vVersion in vQuestions[AIndex][KEY_ANSWERS]:
            if vVersion[KEY_VERSION] == AUserAnswer:
                return vVersion[KEY_VERSION]

    return None

def user_answer(AIndex):
    if vQuestions[AIndex][KEY_KIND] == VALUE_KIND_SELECT:
        vNote = 'Select correct answer and input it\'s index'
    elif vQuestions[AIndex][KEY_KIND] == VALUE_KIND_INPUT:
        vNote = 'Input answer'
    else:
        print('Error! Unknown question type!')
        return None
    
    LUserValue = input(vNote + ' or "q" to exit: ')

    if LUserValue == 'q':
        return None
    else:
        if LUserValue.isnumeric():
            LUserValue = float(LUserValue)
        return LUserValue

vQuestionIndex = -1

while True:
    vQuestionIndex = select_question(vQuestionIndex)

    render_question(vQuestionIndex)

    vUserChoice = user_answer(vQuestionIndex)

    if vUserChoice == None:
        break

    vAnswer = answer_question(vQuestionIndex, vUserChoice)

    if vAnswer != None:
        print(f'\nCongratulations! {vQuestions[vQuestionIndex][KEY_TASK]} {vAnswer}\n')

        vQuestionIndex = -1
    else:
        print('\nSorry. Let\'s try again!\n')
