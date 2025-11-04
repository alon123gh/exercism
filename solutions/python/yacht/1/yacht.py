import  itertools

YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


number_categories  = [ONES, TWOS, THREES, FOURS, FIVES, SIXES]



def score(dice, category):

    if category in number_categories:
        number = number_categories.index(category) + 1
        return number * sum(1 for dice_throw in dice if dice_throw == number)
    if category ==  YACHT and  len(set(dice)) == 1:
        return 50

    dice = sorted(dice)
    groups = [list(group) for _ , group in itertools.groupby(sorted(dice))]
    group_sizes = [len(group) for group in groups]
    if category == FULL_HOUSE and all (group_size in group_sizes for group_size in [2,3]):
        return sum(dice)
    if category == FOUR_OF_A_KIND and any( group_size >=4 for group_size in group_sizes):
        for  group in groups:
              if len(group) >= 4:
                  return sum(group[:4])
    if  category == LITTLE_STRAIGHT and dice == list(range(1,6)):
       return 30

    if category == BIG_STRAIGHT and  dice == list(range(2,7)):
       return 30

    if category == CHOICE:
        return  sum(dice)

    return 0

