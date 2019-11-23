class Answer():

    def __init__(self, question):
        self.choices     = question.choices
        self.user_answer = self.__get_user_answer()

        if self.user_answer == 'q':
            self.user_choice = ''
            self.is_correct  = False
        else:
            self.user_choice = self.__get_user_choice()
            self.is_correct  = self.user_choice.is_correct

    def __get_user_answer(self):
        result = None

        if self.choices.index_mode:
            key_list = tuple([i for i in range(1, len(self.choices) + 1)])
        else:
            key_list = self.choices.get_keys()

        while True:
            user_input = input(f'Select correct answer from list {key_list} and input it or "q" to exit: ')
            user_input = user_input.strip().lower()

            result = user_input

            if len(user_input) == 1:
                if user_input in {'q', 'й'}:
                    result = 'q'
                    break
                elif user_input.isalpha() or user_input in {',', '<'}:
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
                elif user_input.isdigit():
                    result = int(user_input)

            if result in key_list:
                break
            else:
                print('\nWrong format of answer! Try again!\n')

        return result

    def __get_user_choice(self):
        result = None

        if self.choices.index_mode:
            result = self.choices[self.user_answer - 1]
        else:
            for choice in self.choices:
                if choice.key == self.user_answer:
                    result = choice
                    break

        return result

    def display(self):
        print(f'Your answer is: {self.user_answer}) {self.user_choice.value}')

        if self.is_correct:
            print('\nCongratulations!\n')
        else:
            print('\nSorry. Let\'s try again!\n')
