class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def __add__(self, other):
        age = (self.age + other.age) // 10
        name = self.name[:(len(self.name) // 2 + 1)] + other.name[(len(other.name) // 2):]
        surname = f"{self.surname}-{other.surname}"
        return Person(name, surname, age)


def main():
    dad = Person('Seva', 'Levytskyi', 35)
    mom = Person('Liuba', 'Shpat', 34)
    kid = dad + mom
    second = mom + dad + kid
    print(kid.name, kid.surname, kid.age)
    print(second.name, second.surname, second.age)


if __name__ == "__main__":
    main()
