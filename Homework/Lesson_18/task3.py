# Task 3
# Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving
# elements using square brackets syntax.

class SimpleRange:

    def __init__(self, start, end):
        self.__curr = start
        self.__start = start
        self.__end = end
        self.__range = range(start, end)

    def __iter__(self):
        return self

    def __getitem__(self, index):
        result = self.__range.__getitem__(index)
        if isinstance(index, slice):
            return list(result)
        return result

    def __next__(self):
        if self.__curr > self.__end:
            raise StopIteration
        else:
            self.__curr += 1
            return self.__curr - 1

r = SimpleRange(19, 87)
for i in r:
    print(i)

print(r[14])