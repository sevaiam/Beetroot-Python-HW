def main():
    a = input("a = : ")
    b = input("b = : ")
    try:
        print("a + b =", int(a) + int(b))
    except ValueError:
        print("One of the inputs is not a number")


if __name__ == "__main__":
    main()
