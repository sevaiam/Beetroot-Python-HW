"""Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except statement to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?"""


def oops():
    raise KeyError("Index out of bounds")


def main():
    try:
        oops()
    except IndexError:
        print("Caught that error!")


if __name__ == "__main__":
    main()
