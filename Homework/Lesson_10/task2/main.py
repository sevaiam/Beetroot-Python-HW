from helper import print_commands, print_result, read_values, file_check, list_books
from file import read_dataset, write_dataset
from entries import create_entry, update_entry, delete_entry
from search import search
import os
from tabulate import tabulate


# add printing result
def phonebook(dataset_file):
    print_commands()
    while True:
        book = read_dataset(dataset_file)
        # print(book)
        command = input('Введіть команду (c to list commands): ')
        match command:
            case 'n':
                data = read_values(book)
                # print(data)
                if data:
                    book = create_entry(book, data)
                    # print(book)
                    write_dataset(book, dataset_file)
                    print('Entry added.')
                else:
                    print('No data added.')
            case element if element in ['sf', 'sl', 'sfl', 'sp', 'sct', 'sc']:
                query = search(book, command)
                if query:
                    print(f'Found {len(query)} entries:')
                    print_result(query)
                else:
                    print('Found nothing.')
            case 'upd':
                book = update_entry(book)
                if book:
                    write_dataset(book, dataset_file)
            case 'del':
                book = delete_entry(book)
                write_dataset(book, dataset_file)
            case 'exit':
                print('Вихід з програми.')
                break
            case 'c':
                print_commands()
            case 'l':
                if book:
                    print_result(book)
                else:
                    print("No entries in phone book.")
            case _:
                print('Не вірно введена команда.')


if __name__ == '__main__':
    print(tabulate([['Welcome to the BEETROOT task2!']], tablefmt='grid'))
    print('Available phonebooks: ')
    list_books()
    filename = input('Please, enter your task2 name: ')
    file_path = file_check(filename)
    phonebook(file_path)

