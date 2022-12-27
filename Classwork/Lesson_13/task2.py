DEBUG = True


def get_docstring(out=True):
    def get_docstring_dec(func):
        def wrap():
            if out:
                print(f"Function <{func.__name__}\n{func.__doc__}>")
                print('=' * 30)

            func()

        return wrap

    return get_docstring_dec


@get_docstring(DEBUG)
def main():
    """This function does absolutely nothing"""
    print("No")


if __name__ == "__main__":
    main()
