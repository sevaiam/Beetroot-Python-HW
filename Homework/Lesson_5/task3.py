def main():
    hundred = list(range(1, 101))
    selects = []
    i = 0
    while i < len(hundred):
        if hundred[i] % 7 == 0 and hundred[i] % 5:
            selects.append(hundred[i])
        i += 1

    print(selects)


if __name__ == "__main__":
    main()
