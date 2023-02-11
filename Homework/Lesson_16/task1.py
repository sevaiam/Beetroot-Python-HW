# Task 1
# Method overloading.
# Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, and make
# their own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’,
# while Cat’s can be to print ‘meow’.
# Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs
# talk method on input parameter.

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def talk(self):
        pass

class Dog(Animal):

    def talk(self):
        return 'Woof Woof'


class Cat(Animal):

    def talk(self):
        return 'Meow'


dog = Dog()
cat = Cat()


def give_voice(inst):
    return inst.talk()


for pet in (dog, cat):
    print(give_voice(pet))

print(dog.talk())
print(cat.talk())
