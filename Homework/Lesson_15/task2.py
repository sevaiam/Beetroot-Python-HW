# Mathematician
# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

class Mathematician:

    @staticmethod
    def remove_positives(nums: list):
        return [num for num in nums if num < 0]

    @staticmethod
    def filter_leaps(years: list):
        return [year for year in years if year % 4 == 0 and year % 100 != 0 or year % 400 == 0]

    @staticmethod
    def square_nums(nums: list):
        return [num ** 2 for num in nums]


m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020, 2100]))

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
