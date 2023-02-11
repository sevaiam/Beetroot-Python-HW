# Task 3
# Write a class TypeDecorators which has several methods for converting results of functions to a specified type
# (if it's possible):
# methods:
# to_int
# to_str
# to_bool
# to_float
# Don't forget to use @wraps

from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def convert_to_int(*args, **kwargs):
            request = func(func(*args, **kwargs))
            try:
                result = int(request)
                print(f'Converted <{request}> to integer.')
                return result
            except ValueError:
                print(f'Can\'t convert <{request}> to integer.')

        return convert_to_int

    @staticmethod
    def to_str(func):
        @wraps(func)
        def convert_to_str(*args, **kwargs):
            request = func(func(*args, **kwargs))
            try:
                result = str(request)
                print(f'Converted <{request}> to string')
                return result
            except TypeError:
                print(f'Can\'t convert <{request}> to string.')

        return convert_to_str

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def convert_to_bool(*args, **kwargs):
            request = func(func(*args, **kwargs))
            try:
                result = bool(request)
                print(f'Converted <{request}> to boolean')
                return result
            except TypeError:
                print(f'Can\'t convert <{request}> to boolean.')

        return convert_to_bool

    @staticmethod
    def to_float(func):
        @wraps(func)
        def convert_to_float(*args, **kwargs):
            request = func(func(*args, **kwargs))
            try:
                result = float(request)
                print(f'Converted <{request}> to float')
                return result
            except ValueError:
                print(f'Can\'t convert <{request}> to float.')

        return convert_to_float


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


if __name__ == '__main__':
    assert do_nothing('25') == 25
    assert do_something('True') is True
