def main():
    while True:
        country = input('Please enter a country: ')
        if country == 'exit':
            break
        elif country.isalpha():
            print(country.title())
        else:
            print('Not a country')


if __name__ == "__main__":
    main()
