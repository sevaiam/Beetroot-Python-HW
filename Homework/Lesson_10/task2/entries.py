from helper import fields, print_result
from search import search


def create_entry(dataset, data):
    dataset.update(data)
    return dataset


def update_entry(dataset):
    number = input('Please enter phone number to update: ')
    query = search(dataset, 'sp', exact=True, query=number)
    if query:
        print("Enter updated info. Press 'enter' to skip.")
        for k, data in dataset[number].items():
            upd = input(f'New {fields[k]} ({data}): ')
            if upd:
                dataset[number][k] = upd
        print("Updated info: ")
        print_result({number: dataset[number]})
    else:
        print('Number not found')
    # first - search record by number
    # second - read new data
    # third - update record
    return dataset


def delete_entry(dataset):
    number = input('Please enter phone number to delete: ')
    if search(dataset, 'sp', exact=True, query=number):
        confirm = input(f'Are you sure you want to delete entry <{number}>? (Y/n)')
        if confirm.lower() in ('y', 'yes'):
            del dataset[number]
            print(f'Entry <{number}> was removed from phonebook.')
        else:
            print(f'Entry <{number}> was NOT removed from phonebook.')
    else:
        print('Number not found')
    # first - search record by number
    # second - delete record (delete key) del book[number]
    return dataset


if __name__ == '__main__':
    pass
