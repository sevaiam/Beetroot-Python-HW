# Створити генератор текстових емоджі. Емоджі мають починатись там закінчуватись дужками одного й
# того самого типу, в середині містити 3 рандомних символи !@#$^*_-=+?/,.:;~.
from random import choice, choices


class GenEmoji:

    def __init__(self, max):
        self.max = max
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        symbols = '!@#$^*_-=+?/,.:;~.'
        cheeks = (('(', ')'), ('<', '>'), ('|', '|'), ('{', '}'), ('\\', '/'))
        if self.count >= self.max:
            raise StopIteration
        random_cheeks = choice(cheeks)
        random_face = random_cheeks[0] + ''.join(choices(symbols, k=3)) + random_cheeks[1]
        self.count += 1
        return random_face


e = GenEmoji(8)

for i in e:
    print(i)
