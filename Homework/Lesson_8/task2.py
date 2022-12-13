import sys
from pprint import pprint


def main():
    print("Current sys.path:")
    print('=' * 40)
    pprint(sys.path)
    print('=' * 40)
    print()

    print("Trying to import 'stars' module...")
    try:
        import stars
        pprint(dir())
        stars.make_stars()
    except ModuleNotFoundError:
        print('Could not find module in current $PATH.')

    print('Adding a folder to $PATH via sys.path at index 2...')
    print('Checking if the folder was added to $PATH:')
    print('=' * 40)
    sys.path.insert(2, '/Users/seva/Desktop/Py')
    pprint(sys.path)
    print('=' * 40)
    print("Trying to import 'stars' module...")
    try:
        import stars
        pprint(dir())
        print('Imported successfully.')
        stars.make_stars()
    except ModuleNotFoundError:
        print('Could not find module in current $PATH.')


if __name__ == "__main__":
    print('=' * 40)
    print("Beetroot Lesson 8 Task 2 (Seva)")
    print('=' * 40)
    print()
    main()
    print("(I'll debug it later...)")
