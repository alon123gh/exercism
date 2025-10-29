
value_to_letter = {
    1000: "M",
    900:  "CM",
    500:  "D",
    400:  "CD",
    100:  "C",
    90:   "XC",
    50:   "L",
    40:   "XL",
    10:   "X",
    9:    "IX",
    5:    "V",
    4:    "IV",
    1:    "I"
}


def roman(number):
    result = []
    
    while number:
        for value, symbol in value_to_letter.items():
            if number // value != 0:
                number -= value
                result.append(symbol)
                break
    return "".join(result)

