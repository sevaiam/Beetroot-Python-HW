# Fraction
# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною
# перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції порівняння
# між об'єктами класу Fraction

def get_gcd(n1, n2):
    while n1 % n2 != 0:
        n1, n2 = n2, n1 % n2
    return n2


class Fraction:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError('Both numerator and denominator must be integers.')
        elif denominator == 0:
            raise ZeroDivisionError("Denominator can't be zero.")
        else:
            self.numerator = numerator
            self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        gcd = get_gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // gcd, new_denominator // gcd)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        gcd = get_gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // gcd, new_denominator // gcd)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        gcd = get_gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // gcd, new_denominator // gcd)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        gcd = get_gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // gcd, new_denominator // gcd)

    def __eq__(self, other):
        first_n = self.numerator * other.denominator
        second_n = other.numerator * self.denominator
        return first_n == second_n

    def __lt__(self, other):
        first_n = self.numerator * other.denominator
        second_n = other.numerator * self.denominator
        return first_n < second_n

    def __gt__(self, other):
        first_n = self.numerator * other.denominator
        second_n = other.numerator * self.denominator
        return first_n > second_n


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    assert x + y == Fraction(3, 4)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print('x =', x)
    print('y =', y)
