days_of_christmas = [
    ("first", "a Partridge in a Pear Tree"),
    ("second", "two Turtle Doves"),
    ("third", "three French Hens"),
    ("fourth", "four Calling Birds"),
    ("fifth", "five Gold Rings"),
    ("sixth", "six Geese-a-Laying"),
    ("seventh", "seven Swans-a-Swimming"),
    ("eighth", "eight Maids-a-Milking"),
    ("ninth", "nine Ladies Dancing"),
    ("tenth", "ten Lords-a-Leaping"),
    ("eleventh", "eleven Pipers Piping"),
    ("twelfth", "twelve Drummers Drumming"),
]


def add_verse(vers_num, result):

      day = days_of_christmas[vers_num - 1]
      day_part = f"On the {day[0]} day of Christmas my true love gave to me: "
      if vers_num == 1 :
         gifts = f"{day[1]}."
      else:
          day_gifts = [gift for _,gift in days_of_christmas[vers_num-1::-1] ]
          day_gifts[-1] = f"and {day_gifts[-1]}."
          gifts = ", ".join(day_gifts)
      result.append(day_part + gifts)   
    
def recite(start, end):
    result = []
    for verse in range (start, end+1):
        add_verse(verse,result)
    return result