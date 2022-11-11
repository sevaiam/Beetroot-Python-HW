def main():
    name = 'Seva'
    day = 'Saturday'
    print(f'Good day {name}! {day} is a perfect day to learn some python.', '<- using f-string')
    print('Good day ', name, '! ', day, ' is a perfect day to learn some python.', ' <- using several args', sep='')
    print('Good day ' + name + '! ' + day + ' is a perfect day to learn some python.', '<- using concatenation')


if __name__ == "__main__":
    main()
