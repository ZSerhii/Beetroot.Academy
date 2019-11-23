from random import randint
from json   import loads


def from_file(file_path):
    with open(file_path) as json_file:
        json_data = json_file.read()

        return loads(json_data)


class Choice():
    def __init__(self, choice):
        self.id         = choice['id']
        self.content    = choice['content']
        self.is_correct = choice['is_correct']

        item = choice['content'].split(':', 1)

        self.key   = item[0].replace('*', '').lower()
        self.value = item[1].strip()

    def display(self, index_mode = 0):
        if index_mode:
            key = str(int(self.id) + 1)
        else:
            key = self.key

        print(key + ') ' + str(self.is_correct) + ' ' + self.value)


class Choices(list):
    def __init__(self, choices):
        super().__init__(choices)
        self.index_mode = randint(0, 1)

        for index, item in enumerate(self):
            self[index] = Choice(item)

    def display(self):
        for choice in self:
            choice.display(self.index_mode)

    def get_keys(self):
        result = []

        for choice in self:
            result.append(choice.key)

        return tuple(result)


class Question():
    def __init__(self, question):

        self.id      = question['id']
        self.choices = Choices(question['choices'])
        self.content = question['content']

    def display(self):
        print(f'Question №{self.id}\n')
        print(f'{self.content}?\n')
        print('Possible answers:')

        self.choices.display()

        print()


class Questions():
    def __init__(self, questions_path):
        self.list  = from_file(questions_path)
        self.count = len(self.list)

    def get_random_question(self, available_questions):
        questions_id = tuple([id for id, status in available_questions.items() if status == 1])

        question_id = questions_id[randint(0, len(questions_id) - 1)]

        available_questions[question_id] = 0

        return self.get_question_by_id(question_id)

    def get_question_by_id(self, id):
        result = None

        for question in self.list:
            if question['id'] == id:
                result = question
                break

        return Question(result)
