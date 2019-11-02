import json
import os.path

PATH = 'c:\\Projects\\Beetroot.Academy\\Lessons\\'

def do_task():
    task = '\nTask 1: \nSaving progress.\n' \
           'Make a function that takes personal information as arguments, e.g., name,\n' \
           'last name, phone number, address, etc. Then make another function that\n' \
           '"saves the data onto a file. Make sure that it works by checking that the\n' \
           'file was created and that it contains the right data.\n'
    
    print(task)

    def get_data(a_data_kind, a_data_value):
        return json.dumps({a_data_kind: a_data_value})

    def save_data_to_file(a_data):
        with open(PATH + 'HW10.txt', 'a') as txt_file:
            txt_file.write('\n' + get_data('name', 'Serhii'))

    def check_data_in_file(a_data):
        result = False

        if os.path.isfile(PATH +'HW10.txt'):
            with open(PATH +'HW10.txt') as txt_file:
                txt_rows = txt_file.readlines()

            result = a_data in txt_rows
        else:
            print('File not found')

            result = False

        return result

    print('Result 1:\n')

    data = get_data('name', 'Serhii')

    save_data_to_file(data)

    print(f'Is data "{data}" containing in the file:', check_data_in_file(data))

    task = '\nTask 2: \nAdd to the previous program a function for opening up the same file which the data was saved on. \n' \
           'Make sure that it works by making the function print out the data.\n'   

    print(task)

    def print_file_content():
        if os.path.isfile(PATH +'HW10.txt'):
            with open(PATH +'HW10.txt') as txt_file:
                for line in txt_file: 
                    print(line.strip())
        else:
            print('File not found')

    print('Result 2:\n')

    print_file_content()

def main():
    do_task()

    return 0

exit(main())