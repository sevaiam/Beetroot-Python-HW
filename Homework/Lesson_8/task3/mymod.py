def count_lines(name: str) -> int:
    with open(name, 'r') as file:
        return len(file.readlines())


def count_chars(name: str) -> int:
    with open(name, 'r') as file:
        return len(file.read())


def test(name):
    print(count_lines(name))
    print(count_chars(name))


if __name__ == "__main__":
    test('mymod.py')
