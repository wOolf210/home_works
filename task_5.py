class Roman:
    roman_numerals = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL",
        50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"
    }

    def __init__(self, value):
        self.value = value

    @staticmethod
    def int_to_roman(num):
        result = ""
        for value, numeral in sorted(Roman.roman_numerals.items(), reverse=True):
            while num >= value:
                result += numeral
                num -= value
        return result

    @staticmethod
    def roman_to_int(roman):
        roman_dict = {v: k for k, v in Roman.roman_numerals.items()}
        total = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i+2] in roman_dict:
                total += roman_dict[roman[i:i+2]]
                i += 2
            else:
                total += roman_dict[roman[i]]
                i += 1
        return total

    def __add__(self, other):
        return Roman(self.value + other.value)

    def __sub__(self, other):
        return Roman(self.value - other.value)

    def __mul__(self, other):
        return Roman(self.value * other.value)

    def __truediv__(self, other):
        return Roman(self.value // other.value)

    def __str__(self):
        return Roman.int_to_roman(self.value)

    def display(self):
        print(f"Римское число: {self}, целое число: {self.value}")


if __name__ == "__main__":
    roman1 = Roman(10)
    roman2 = Roman(5)

    roman1.display()
    roman2.display()

    roman3 = roman1 + roman2
    roman3.display()

    roman4 = roman1 - roman2
    roman4.display()
