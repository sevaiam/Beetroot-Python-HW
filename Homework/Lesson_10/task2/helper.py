from file import read_dataset, write_dataset
import sys, os
from tabulate import tabulate

base_dict = {'phone_number': {'first_name': '',
                              'last_name': '',
                              'city': '',
                              'country': ''}}

fields = {
    'phone_number': 'номер телефону',
    'first_name': 'ім\'я',
    'last_name': 'прізвище',
    'city': 'місто',
    'country': 'країна',
    'full_name': 'full name'
}

options = {
    "l": "list all entries",
    "n": "створити новий запис",
    "sf": "пошук за ім'ям",
    "sl": "пошук за прізвищем",
    "sfl": "пошук за повним ім'ям",
    "sp": "пошук за телефоном",
    "sct": "пошук за містом",
    "sc": "пошук за країною",
    "upd": "оновлення запису",
    "del": "видалити запис",
    "exit": "вихід з програми",
}


def print_commands():
    print('=' * 30)
    print("Достyпні команди:")
    for option in options:
        print(f'{option} - {options[option]}')
    print('=' * 30)


def print_result(results):
    headers = [fields['phone_number'].capitalize()] + [fields[k].capitalize() for k, v in base_dict['phone_number'].items()]
    table = []
    for phone, data in results.items():
        row = [phone]
        for field in data:
            row.append(results[phone][field])
        table.append(row)
    print(tabulate(table, headers=headers, tablefmt="grid"))
    # for record in result_list:
    # for phone in results:
    #     for key, value in zip(keys, values):
    #         if key == 'phone_number':
    #             print(f'{value.capitalize()}: {phone}')
    #         else:
    #             print(f'{value.capitalize()}: {results[phone][key]}')


def read_values(dataset={}):
    new_data = {}
    phone = ''
    for key, value in base_dict.items():
        phone = input(f'Введіть {fields[key]}: ')
        if phone in dataset:
            print('Phone already in the task2.')
            return
        new_data[phone] = {}
        for v in value:
            new_data[phone][v] = input(f'Введіть {fields[v]}: ')
    return new_data


def file_check(filename):
    try:
        dataset = read_dataset(f'files/{filename}.json')
    except FileNotFoundError:
        newfile = input('File not found. Do you want to create one? [Y/n] ').lower()
        if newfile in ('y', 'yes'):
            # new_filename = input("Please, enter the name for your new task2: ")
            file_path = f'files/{filename}.json'
            write_dataset(dict(), file_path)
            print('Phonebook created.')
            return file_path
        else:
            print('Thanks for using our task2!')
            sys.exit()
    return f'files/{filename}.json'


def list_books():
    for name in os.listdir('files'):
        if name.endswith('.json'):
            print(f'<{name[:-5]}> ', end='')
    print()


if __name__ == '__main__':
    print(read_values())
