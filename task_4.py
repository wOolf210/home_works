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


class SubClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self._number = number

    def get_number(self):
        return self._number

    def set_number(self, number):
        self._number = number


if __name__ == "__main__":
    main_object = MainClass("Hello")
    print(main_object.get_text())

    main_object.set_text("New text")
    print(main_object.get_text())

    sub_object = SubClass("SubClass Text", 42)
    print(sub_object.get_text())
    print(sub_object.get_number())
