import re

color_translate = {
    "black" : "0",
    "brown" : "1",
    "red" : "2",
    "orange" : "3",
    "yellow" : "4",
    "green" : "5",
    "blue" : "6",
    "violet" : "7",
    "grey" : "8",
    "white" : "9",
}

def label(colors):

    
    label_str = "".join([color_translate.get(color) for color in colors[:2]]) 
    label_str = re.sub("^0(?=\d+)", "", label_str)
    label_str += "0" * int(color_translate.get(colors[2]))
    if label_str.endswith("0"*9):
        return label_str[:-9] + " gigaohms"
    elif label_str.endswith("0"*6):
        return label_str[:-6] + " megaohms"     
    elif label_str.endswith("0"*3):
        return label_str[:-3] + " kiloohms"          
    return label_str + " ohms"
