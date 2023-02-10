# Task 1
# Write a Python program to detect the number of local variables declared in a function.

def task1_func():
    hi = 'hi'
    greet = 'hello world'
    x = 3
    y = 5

    def inner_func():
        z = 9

    return


task1 = task1_func

print(f'Function "{task1.__name__}" has {task1.__code__.co_nlocals} variables.')
