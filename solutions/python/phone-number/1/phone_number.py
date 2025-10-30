import re
from string import punctuation
from string import ascii_lowercase

invalid_punctuations = set(punctuation) - set("()+-.")


class PhoneNumber:
    def __init__(self, raw_number):
        self.raw_number = raw_number
        self.country_code = None
        self.area_code = None
        self.exchange_code = None
        self.local_number = None
        self.number = None
        self.validate()
        self.compose_number()

    def validate(self):
        number_symbols_list = list(self.raw_number.lower())

        if any(symbol in ascii_lowercase for symbol in number_symbols_list):
            raise ValueError("letters not permitted")
        if any(symbol in invalid_punctuations for symbol in number_symbols_list):
            raise ValueError("punctuations not permitted")


        digits = [symbol for symbol in number_symbols_list if symbol.isdigit()]
        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits)  > 11:
            raise ValueError("must not be greater than 11 digits")

        if len(digits)  == 11 and digits[0] != "1":
            raise ValueError("11 digits must start with 1")

        if not self.extract_number():
            raise ValueError("number could not be parsed " + self.raw_number)

        invalid_numbers = [("0", "zero"), ("1", "one")]
        for number, number_name in invalid_numbers:
            if self.exchange_code.startswith(number):
                raise ValueError(f"exchange code cannot start with {number_name}")
            if self.area_code.startswith(number):
                raise ValueError(f"area code cannot start with {number_name}")


    def extract_number(self):
        number_pattern = re.compile(r"\+*(1*)[^0-9]*([0-9]{3})[^0-9]*([0-9]{3})[^0-9]*([0-9]{4})")
        m = number_pattern.match(self.raw_number)
        if m:
            self.country_code = m.group(1)
            self.area_code = m.group(2)
            self.exchange_code = m.group(3)
            self.local_number = m.group(4)
            return True
        return False

    def compose_number(self):
        self.number = f"{self.area_code}{self.exchange_code}{self.local_number}"
        
    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.local_number}"

