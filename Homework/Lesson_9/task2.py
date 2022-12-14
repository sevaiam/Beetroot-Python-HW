"""
Write a function that takes in two numbers from the user via input(), call the numbers a and b,
and then returns the value of squared a divided by b, construct a try-except block which raises an exception
if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).
"""


def main():
    a = input("a = ")
    b = input("b = ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("One of the values is not an int")
        return
    try:
        print(a ** 2 / b)
    except ZeroDivisionError:
        print("Can't divide by zero!")


if __name__ == "__main__":
    main()
