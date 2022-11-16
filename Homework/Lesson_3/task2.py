def check_phone(s: str) -> bool:
    return s.isdigit() and len(s) == 10


def main():
    number = input("Please, input a phone number: ")
    if check_phone(number):
        print("That's a phone number all right!")
    else:
        print("Seems like it's not a phone number at all.")


if __name__ == "__main__":
    main()
