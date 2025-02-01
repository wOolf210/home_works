class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


class CircleInSquare(Circle, Square):
    def __init__(self, radius, side_length):
        Circle.__init__(self, radius)
        Square.__init__(self, side_length)

    def display_area(self):
        print(f"Площадь окружности: {self.area()} кв. единиц")
        print(f"Площадь квадрата: {self.area()} кв. единиц")


if __name__ == "__main__":
    circle_in_square = CircleInSquare(5, 10)
    circle_in_square.display_area()
