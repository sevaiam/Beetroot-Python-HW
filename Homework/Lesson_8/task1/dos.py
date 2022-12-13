import cowsay


def say():
    name = input("Please enter your name:\n")
    cowsay.daemon(f"Hi, {name}!")


if __name__ == "__main__":
    say()
