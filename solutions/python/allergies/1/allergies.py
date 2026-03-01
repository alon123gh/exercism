

ALLERGENS = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128,
}


class Allergies:

    def __init__(self, score):
        self.score = score & 0xFFFFFFFF

    def allergic_to(self, item):
        alegran_id = ALLERGENS.get(item, 0)
        return (self.score & alegran_id) != 0


    @property
    def lst(self):
        return [key for key,item in ALLERGENS.items() if (item & self.score !=0) ] 
