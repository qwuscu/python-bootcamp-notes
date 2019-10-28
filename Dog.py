from Animal import *


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

my_dog = Dog()
