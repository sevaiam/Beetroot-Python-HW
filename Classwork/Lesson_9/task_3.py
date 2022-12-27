class IsNotEven(Exception):
    pass


def is_even(n):
    if n % 2 == 0:
        return "It's even!"
    else:
        raise IsNotEven("Nope, that's not an even number")


def main():
    num = input("Please enter an even number: ")
    try:
        print(is_even(int(num)))
    except ValueError:
        print("That's not a number at all!")


if __name__ == "__main__":
    main()
