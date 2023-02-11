# Task 1
# Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
# `iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function

def with_index(iterable, start=0):
    for i in range(len(iterable)):
        yield start, iterable[i]
        start += 1

li = ['foo', 'bar', 'baz']

for no, item in with_index(li, 2):
    print(no, item)
