# Task 2
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
from functools import wraps

stopwords = ['pepsi', 'BMW']


def stop_words(words: list):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            clean_str = func(*args, **kwargs)
            for word in words:
                if word in clean_str:
                    clean_str = clean_str.replace(word, '*')
            return clean_str
        return wrapper
    return inner


@stop_words(stopwords)
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW !'


print(create_slogan('Steve'))
assert create_slogan('Steve') == 'Steve drinks * in his brand new * !'
