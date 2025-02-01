class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)

    def display(self):
        print(f"{self.real} + {self.imag}i")


if __name__ == "__main__":
    c1 = Complex(3, 4)
    c2 = Complex(1, 2)

    c3 = c1 + c2
    c3.display()

    c4 = c1 - c2
    c4.display()

    c5 = c1 * c2
    c5.display()

    c6 = c1 / c2
    c6.display()
