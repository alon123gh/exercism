import string

class Luhn:
    def __init__(self, card_num):
        self.digit_list = None
        self.card_num = card_num

    @staticmethod
    def multiple(num):
        num *= 2
        return num - 9  if num > 9 else num

    def valid(self):

        self.card_num = self.card_num.replace(" ", "")           
        if any(not symbol.isdigit() for symbol in list(self.card_num )):
            return False

        self.digit_list = [int(digit) for digit in list(self.card_num)]
        
        if len(self.digit_list) < 2:
            return False
          
        for i in range(len(self.digit_list) - 2, -1, -2):
            self.digit_list[i] = Luhn.multiple(self.digit_list[i])

        return sum(self.digit_list) % 10 == 0