import pickle


class Shape:
    def show(self):
        pass

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)


class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def show(self):
        return f"Квадрат: ({self.x}, {self.y}), сторона: {self.side_length}"


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        return f"Прямоугольник: ({self.x}, {self.y}), ширина: {self.width}, высота: {self.height}"


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        return f"Окружность: ({self.x}, {self.y}), радиус: {self.radius}"


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        return f"Эллипс: ({self.x}, {self.y}), ширина: {self.width}, высота: {self.height}"


if __name__ == "__main__":
    shapes = [
        Square(0, 0, 10),
        Rectangle(0, 0, 20, 10),
        Circle(0, 0, 15),
        Ellipse(0, 0, 30, 15)
    ]

    for shape in shapes:
        print(shape.show())

    with open('shapes.pkl', 'wb') as f:
        pickle.dump(shapes, f)

    with open('shapes.pkl', 'rb') as f:
        loaded_shapes = pickle.load(f)

    print("\nЗагруженные фигуры:")
    for shape in loaded_shapes:
        print(shape.show())
