class Stadium:
    def __init__(self, name="", opening_date="", country="", city="", capacity=0):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Введите название стадиона: ")
        self.opening_date = input("Введите дату открытия: ")
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = int(input("Введите вместимость: "))

    def display_data(self):
        print(f"Название стадиона: {self.name}")
        print(f"Дата открытия: {self.opening_date}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Вместимость: {self.capacity}")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_opening_date(self):
        return self.opening_date

    def set_opening_date(self, opening_date):
        self.opening_date = opening_date

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity


if __name__ == "__main__":
    stadium = Stadium()
    stadium.input_data()
    stadium.display_data()
