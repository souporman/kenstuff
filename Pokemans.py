class Pet():
    """Represents a pet."""

    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print("Noise!")


class Cat(Pet):
    """Represents a cat - a type of pet"""


cat1 = Cat("Sushi")
cat1.make_noise()
