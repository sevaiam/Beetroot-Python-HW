from math import tan, pi
from random import randint, choice

class Figure:
    def __init__(self, sides: int, side_length: int):
        self.sides = sides
        self.side_length = side_length
        self.angle = float(pi / float(sides))
        self.apotema = (float(side_length) / 2) / tan(self.angle)

    def area(self):
        return round((self.sides * self.side_length * self.apotema) / 2, 2)


class Triangle(Figure):
    def __init__(self, side_length):
        super().__init__(3, side_length)

class Square(Figure):
    def __init__(self, side_length):
        super().__init__(4, side_length)


class Calculator:
    def __init__(self):
        self.figures = [Figure, Triangle, Square]

    def generate(self, figure_number):
        for _ in range(figure_number):
            figure = choice(self.figures)
            length = randint(2, 11)
            if figure is Figure:
                sides = randint(2, 11)
                




f = Triangle(3)
print(f.area())