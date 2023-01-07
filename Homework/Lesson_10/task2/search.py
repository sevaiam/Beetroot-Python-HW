from helper import print_result, fields


def search(dataset, parameters, exact=False, query=''):
    match parameters:
        case 'sp':
            param = 'phone_number'
        case 'sf':
            param = 'first_name'
        case 'sl':
            param = 'last_name'
        case 'sfl':
            param = 'full_name'
        case 'sct':
            param = 'city'
        case 'sc':
            param = 'country'
        case _:
            param = 'phone_number'

    query_dataset = {}
    if not query:
        query = input(f'Please, enter {fields[param]} to search: ').lower()

    for phone, data in dataset.items():
        if exact:
            if param == 'phone_number':
                if query == phone:
                    query_dataset[phone] = data
            elif query == data[param].lower():
                query_dataset[phone] = data
        else:
            if param == 'phone_number':
                if query in phone:
                    query_dataset[phone] = data
            if param == 'full_name':
                fullname = query.split()
                # print(fullname)
                # print(data)
                if len(fullname) != 2:
                    print('Invalid full name')
                    return query_dataset
                if fullname[0] in data['first_name'].lower() and fullname[1] in data['last_name'].lower():
                    query_dataset[phone] = data
                elif fullname[1] in data['first_name'].lower() and fullname[0] in data['last_name'].lower():
                    query_dataset[phone] = data
            elif query in data[param].lower():
                query_dataset[phone] = data

    return query_dataset


if __name__ == '__main__':
    pass
