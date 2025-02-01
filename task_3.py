class Airplane:
    def __init__(self, model, max_passengers):
        self.model = model
        self.max_passengers = max_passengers

    def __eq__(self, other):
        return self.model == other.model

    def __add__(self, num):
        self.max_passengers += num
        return self

    def __sub__(self, num):
        self.max_passengers -= num
        return self

    def __iadd__(self, num):
        self.max_passengers += num
        return self

    def __isub__(self, num):
        self.max_passengers -= num
        return self

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def display(self):
        print(f"Самолет {self.model} имеет вместимость {self.max_passengers} пассажиров.")


if __name__ == "__main__":
    airplane1 = Airplane("Boeing 737", 200)
    airplane2 = Airplane("Airbus A320", 180)

    airplane1.display()
    airplane2.display()

    print(airplane1 == airplane2)
    print(airplane1 > airplane2)

    airplane1 += 20
    airplane1.display()

    airplane2 -= 10
    airplane2.display()
