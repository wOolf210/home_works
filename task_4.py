class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price

    def display(self):
        print(f"Квартира с площадью {self.area} м² и ценой {self.price}.")


if __name__ == "__main__":
    flat1 = Flat(50, 300000)
    flat2 = Flat(60, 350000)

    flat1.display()
    flat2.display()

    print(flat1 == flat2)
    print(flat1 != flat2)

    print(flat1 > flat2)
    print(flat1 < flat2)
