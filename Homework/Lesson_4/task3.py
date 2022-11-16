from random import shuffle


def main():
    word = [x for x in input("Please, enter a word: ")]
    # print(word)
    for _ in range(5):
        shuffle(word)
        print(''.join(word))


if __name__ == "__main__":
    main()
