class Ship:
    def __init__(self, name, year, country):
        self.name = name
        self.year = year
        self.country = country

    def display_info(self):
        print(f"Корабль: {self.name}")
        print(f"Год постройки: {self.year}")
        print(f"Страна: {self.country}")


class Frigate(Ship):
    def __init__(self, name, year, country, weapon_type):
        super().__init__(name, year, country)
        self.weapon_type = weapon_type

    def fire_weapon(self):
        print("Фрегат открывает огонь!")

    def display_info(self):
        super().display_info()
        print(f"Тип оружия: {self.weapon_type}")


class Destroyer(Ship):
    def __init__(self, name, year, country, missile_type):
        super().__init__(name, year, country)
        self.missile_type = missile_type

    def launch_missile(self):
        print("Эсминец запускает ракету!")

    def display_info(self):
        super().display_info()
        print(f"Тип ракеты: {self.missile_type}")


class Cruiser(Ship):
    def __init__(self, name, year, country, armor):
        super().__init__(name, year, country)
        self.armor = armor

    def engage_combat(self):
        print("Крейсер вступает в бой!")

    def display_info(self):
        super().display_info()
        print(f"Броня: {self.armor}")


if __name__ == "__main__":
    frigate = Frigate("Фрегат-1", 2010, "Россия", "Ракетное оружие")
    destroyer = Destroyer("Эсминец-1", 2015, "США", "Томагавк")
    cruiser = Cruiser("Крейсер-1", 2000, "Китай", "Толстая сталь")

    frigate.display_info()
    destroyer.display_info()
    cruiser.display_info()
