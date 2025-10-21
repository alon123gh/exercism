NUMBERS_1_TO_19 = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen"
}

TENS = {
    2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
    6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
}

GROUP_NAMES = ["", "thousand", "million", "billion"]


def two_digit(num: int) -> str:
    if num == 0:
        return ""
    if num < 20:
        return NUMBERS_1_TO_19[num]
    tens, ones = divmod(num, 10)
    return TENS[tens] + (f"-{NUMBERS_1_TO_19[ones]}" if ones else "")


def three_digit(num: int) -> str:
    if num == 0:
        return ""
    hundreds, remainder = divmod(num, 100)
    words = []
    if hundreds:
        words.append(f"{NUMBERS_1_TO_19[hundreds]} hundred")
    if remainder:
        words.append(two_digit(remainder))
    return " ".join(words)


def say(num) :
    if num < 0 or num >  999_999_999_999:
        raise ValueError("input out of range") 
       
    if num == 0:
        return "zero"

    words = []
    for group_name in GROUP_NAMES:
        num, chunk = divmod(num, 1000)
        if chunk:
            part = three_digit(chunk)
            if group_name:
                part += f" {group_name}"
            words.insert(0, part)
        if num == 0:
            break

    return " ".join(words).strip()

