class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

    def show_wheels(self):
        print(f"Колеса: {self.wheel_count}")


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def show_engine(self):
        print(f"Двигатель: {self.engine_type}")


class Doors:
    def __init__(self, door_count):
        self.door_count = door_count

    def show_doors(self):
        print(f"Двери: {self.door_count}")


class Car(Wheels, Engine, Doors):
    def __init__(self, wheel_count, engine_type, door_count):
        Wheels.__init__(self, wheel_count)
        Engine.__init__(self, engine_type)
        Doors.__init__(self, door_count)

    def display_car_info(self):
        self.show_wheels()
        self.show_engine()
        self.show_doors()


if __name__ == "__main__":
    car = Car(4, "Бензиновый", 4)
    car.display_car_info()
