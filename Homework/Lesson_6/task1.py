def main():
    sentence = input("Please, enter a sentence to count: ").replace(',', '').replace('.', '').split()
    dic = {}
    for i in sentence:
        dic.setdefault(i, 0)
        dic[i] += 1

    return dic


if __name__ == "__main__":
    print(main())
