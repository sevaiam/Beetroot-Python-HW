# Task 1
# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Function <{func.__name__}> was called with <{args}> as arguments.')
    return wrapper


@logger
def add(x: int, y: int):
    return x + y


@logger
def square_list(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_list(4, 5, 6, 7)