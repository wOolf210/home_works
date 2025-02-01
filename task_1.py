class Device:
    def __init__(self, name, brand, power):
        self.name = name
        self.brand = brand
        self.power = power

    def display_info(self):
        print(f"Устройство: {self.name}")
        print(f"Бренд: {self.brand}")
        print(f"Мощность: {self.power} Вт")


class CoffeeMachine(Device):
    def __init__(self, name, brand, power, capacity):
        super().__init__(name, brand, power)
        self.capacity = capacity

    def brew_coffee(self):
        print("Приготовление кофе...")

    def display_info(self):
        super().display_info()
        print(f"Емкость: {self.capacity} литров")


class Blender(Device):
    def __init__(self, name, brand, power, speed):
        super().__init__(name, brand, power)
        self.speed = speed

    def blend(self):
        print("Взбивание ингредиентов...")

    def display_info(self):
        super().display_info()
        print(f"Скорость: {self.speed} оборотов в минуту")


class MeatGrinder(Device):
    def __init__(self, name, brand, power, grind_size):
        super().__init__(name, brand, power)
        self.grind_size = grind_size

    def grind_meat(self):
        print("Измельчение мяса...")

    def display_info(self):
        super().display_info()
        print(f"Размер измельчения: {self.grind_size}")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine("Кофемашина", "DeLonghi", 1500, 1.5)
    blender = Blender("Блендер", "Philips", 600, 22000)
    meat_grinder = MeatGrinder("Мясорубка", "Bosch", 1200, "Средний")

    coffee_machine.display_info()
    blender.display_info()
    meat_grinder.display_info()
