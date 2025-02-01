class MainClass:
    def __init__(self, text=""):
        self._text = text

    def set_text(self, text=None):
        if text is not None:
            self._text = text
        else:
            self._text = "Значение не задано"

    def get_text(self):
        return self._text

    def display_info(self):
        return f"Текст: {self._text}"


class SubClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self._number = number

    def set_number(self, number):
        self._number = number

    def get_number(self):
        return self._number

    def display_info(self):
        return f"Текст: {self._text}, Число: {self._number}"


if __name__ == "__main__":
    text = input("Введите текст для главного класса: ")
    main_object = MainClass(text)
    print(main_object.display_info())

    text = input("Введите новый текст для главного класса: ")
    main_object.set_text(text)
    print(main_object.display_info())

    text = input("Введите текст для класса потомка: ")
    number = int(input("Введите число для класса потомка: "))
    sub_object = SubClass(text, number)
    print(sub_object.display_info())

    number = int(input("Введите новое число для класса потомка: "))
    sub_object.set_number(number)
    print(sub_object.display_info())
