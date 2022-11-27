from random import randint

def main():
    numbers = []
    i = 0
    while i < 10:
        numbers.append(randint(0, 100))
        i += 1

    print(max(numbers))


if __name__ == "__main__":
    main()
