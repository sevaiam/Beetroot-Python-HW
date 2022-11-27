def main():
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
    totals = {}

    for i in stock:
        totals[i] = stock[i] * prices[i]

    return totals


if __name__ == "__main__":
    print(main())
