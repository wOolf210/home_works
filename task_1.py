import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.get_circumference() < other.get_circumference()

    def __le__(self, other):
        return self.get_circumference() <= other.get_circumference()

    def __gt__(self, other):
        return self.get_circumference() > other.get_circumference()

    def __ge__(self, other):
        return self.get_circumference() >= other.get_circumference()

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __isub__(self, other):
        self.radius -= other.radius
        return self

    def get_circumference(self):
        return 2 * math.pi * self.radius

    def display(self):
        print(f"Окружность с радиусом {self.radius} имеет длину {self.get_circumference()}.")


if __name__ == "__main__":
    circle1 = Circle(5)
    circle2 = Circle(3)
    circle1.display()
    circle2.display()

    print(circle1 == circle2)
    print(circle1 > circle2)

    circle3 = circle1 + circle2
    circle3.display()

    circle1 += circle2
    circle1.display()
