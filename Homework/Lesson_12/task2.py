# Task 2
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def multiply_by(multiplier):
    def multiply_func(num):
        return num * multiplier
    return multiply_func

x_6 = multiply_by(6)

print(x_6(11))
