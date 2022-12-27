def main():
    with open('numbers.txt', 'w') as file:
        for i in range(1, 11):
            file.write(str(i) + '\n')

    numbers_sum = 0

    with open('numbers.txt', 'r') as file:
        for line in file.readlines():
            numbers_sum += int(line)

    print(numbers_sum)

    with open('sum_numbers.txt', 'w') as file:
        file.write(str(numbers_sum))


if __name__ == "__main__":
    main()
