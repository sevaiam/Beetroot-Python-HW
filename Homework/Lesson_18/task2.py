# Task 2
# Create your own implementation of a built-in function range, named in_range(), which takes three parameters: `start`,
# `end`, and optional step. Tips: See the documentation for `range` function

def in_range(start: int, end: int, step=1):
    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step
    else:
        raise ValueError('You should use non-zero integer.')


countdown = in_range(87, 19, -2)
for item in countdown:
    print(item)
