import random
from string import  ascii_uppercase

class Robot:

    all_names = []

    def __init__(self):
        self.name = None
        self.gen_name()


    def gen_name(self):
        while True:
            letters_list = list(ascii_uppercase)
            random.shuffle(letters_list)
            letters = letters_list[:2]
            numbers = [str(random.randint(0,9)) for _  in range(3) ]
            name =  "".join(letters) + "".join(numbers)
            if name not in Robot.all_names:
                Robot.all_names.append(name)
                self.name = name
                break

    def reset(self):
        self.gen_name()




