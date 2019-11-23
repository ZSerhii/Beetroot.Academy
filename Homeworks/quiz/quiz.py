from questions import Questions
from answers   import Answer


QUESTIONS_PATH = 'C:\\Projects\\Beetroot.Academy\\Lessons\\questions.json'

KEY_PROGRESS_SUCCESSES = 1
KEY_PROGRESS_MISTAKES  = 0


def render_user_progress(user_progress, available_questions):
    remain_questions = tuple([id for id, status in available_questions.items() if status == 1])
    passed_questions = user_progress[KEY_PROGRESS_SUCCESSES] + user_progress[KEY_PROGRESS_MISTAKES]

    return (f'Questions: {passed_questions}, ' +
            f'correct answers: {user_progress[KEY_PROGRESS_SUCCESSES]}, ' +
            f'mistakes: {user_progress[KEY_PROGRESS_MISTAKES]}. ' +
            f'Questions left: {len(remain_questions)}.\n')


def run_quiz():
    questions     = Questions(QUESTIONS_PATH)
    user_progress = {KEY_PROGRESS_SUCCESSES: 0,
                     KEY_PROGRESS_MISTAKES:  0}

    available_questions = {question['id']: 1 for question in questions.list}

    print('Welcome! Let the game begin!\n')

    question    = questions.get_random_question(available_questions)
    need_repeat = False

    while True:
        question.display()

        answer = Answer(question)

        if answer.user_answer == 'q':
            print('\nGoodbye! We\'ll miss you :(\n')
            break
        else:
            if answer.is_correct:
                question = questions.get_random_question(available_questions)

            if not need_repeat:
                user_progress[answer.is_correct] += 1

            need_repeat = not answer.is_correct

            answer.display()

            print(render_user_progress(user_progress, available_questions))

    exit()


if __name__ == '__main__':
    run_quiz()
