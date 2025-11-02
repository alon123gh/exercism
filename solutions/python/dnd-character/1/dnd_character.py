import random


def roll_4():
    rolls = [random.randint(1,6) for _ in range (1,4)]
    return sum(sorted(rolls)[1:])


class Character:

    abilities = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    
    def __init__(self):

        self.strength = roll_4()
        self.dexterity = roll_4()
        self.constitution = roll_4()
        self.intelligence = roll_4()
        self.wisdom = roll_4()
        self.charisma = roll_4()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        
        ability = random.choice(Character.abilities)
        return getattr(self,ability)
        
        
    
def modifier(value):

    return  (value - 10)//2
