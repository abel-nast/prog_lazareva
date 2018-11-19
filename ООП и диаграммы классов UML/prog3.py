class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("I am Animal.")


class Zebra(Animal):
    def __init__(self, name, age, number_of_stripes):
        super().__init__(name, age)
        print("I am Zebra.")
        print("I am " + name + ".")
        print("I am " + str(age) + ".")
        print("I have " + str(number_of_stripes) + " stripes on my body.")


class Dolphin(Animal):
    def __init__(self, name, age, fishes):
        super().__init__(name, age)
        print("I am Dolphin.")
        print("I am " + name + ".")
        print("I am " + str(age) + ".")
        print("I ate " + str(fishes) + " fishes.")


na = "Vasya"
ag = 10
num = 50
fish = 15
d = Dolphin(na, ag, fish)
z = Zebra(na, ag, num)
