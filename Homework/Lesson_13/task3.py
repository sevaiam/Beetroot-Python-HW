# Task 3
# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False, the function should return False and print the reason it failed;
# otherwise, return the result.

from functools import wraps


def arg_rules(type_: type, max_length: int, contains: list):
    def inner(func):
        @wraps(func)
        def wrapper(str_):
            if type(str_) != type_:
                print(f'Wrong data type (should be {type_}).')
                return False
            if len(str_) > max_length:
                print(f'String exceeds max length ({max_length}).')
                return False
            for symbol in contains:
                if symbol not in contains:
                    print('String doesn\'t contain required symbols.')
                    return False
            return func(str_)

        return wrapper

    return inner


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW !'


print(create_slogan('johndoe05gmail.com'))
print(create_slogan('S@SH05'))
