def is_armstrong_number(number):
    digits = list(str(number))
    power = len(digits)
    return sum(int(digit)**power for digit in digits) == number

