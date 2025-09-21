import math

def score(x, y):
    score = 0
    radius =  math.hypot(x,y)
    if radius <= 1:
        score = 10
    elif 1 < radius <= 5:
        score = 5
    elif 5 < radius <= 10:
        score = 1
    return score
