def make_operation(operand: str, *args: int) -> int:
    if len(args) < 2:
        print('Not enough arguments.')
        return None
    result = args[0]
    if operand == '+':
        for arg in args[1:]:
            result += arg
    elif operand == '-':
        for arg in args[1:]:
            result -= arg
    elif operand == '*':
        for arg in args[1:]:
            result *= arg
    else:
        print('Invalid operand.')
        return None
    return result


def main():
    print('2 + 2 is', make_operation('+', 2, 2))
    print('7 + 7 + 2 is', make_operation('+', 7, 7, 2))
    print('5 - 5 - (-10) - (-20) is', make_operation('-', 5, 5, -10, -20))
    print('7 * 6 is', make_operation('*', 7, 6))


if __name__ == "__main__":
    main()
