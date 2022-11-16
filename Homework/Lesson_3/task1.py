def string_ends(s: str):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]


def main():
    print(string_ends('x'))


if __name__ == "__main__":
    main()
