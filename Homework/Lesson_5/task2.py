from random import randint


def main():
    numbers_1 = []
    numbers_2 = []
    i = 0
    while i < 10:
        numbers_1.append(randint(1, 10))
        numbers_2.append(randint(1, 10))
        i += 1

    print(list(set([x for x in numbers_1 if x in numbers_2])))


if __name__ == "__main__":
    main()
