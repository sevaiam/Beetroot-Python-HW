# Task 2
# Doggy age
# Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.


class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return f'{self.age} dog years is equal to {self.age * self.age_factor} human years. WOOF!'


laika = Dog(10)
print(laika.human_age())
