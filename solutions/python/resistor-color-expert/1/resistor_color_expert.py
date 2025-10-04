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

tolerance_translate = {
    "grey"  : "0.05%",
    "violet"  : "0.1%",
    "blue"  : "0.25%",
    "green"  : "0.5%",
    "brown"  : "1%",
    "red"  : "2%",
    "gold"  : "5%",
    "silver"  : "10%",
}

def get_val_num(input_size):
    val_num = 1
    if input_size == 5:
        val_num = 3
    elif input_size == 4:        
        val_num = 2
    return val_num

def format_values(val):
    val_unit = ""
    for val_limit, unit in [(1e9, "giga"), (1e6, "mega") , (1e3,"kilo") ]:
          if val >= val_limit:
              val = val/val_limit
              val_unit = unit
              break
    return f"{val:g} {val_unit}ohms"          
              
def resistor_label(colors):

   
    input_size = len(colors)
    val_num = get_val_num(input_size)
    label_str = "".join([color_translate.get(color) for color in colors[:val_num]]) 
    if val_num > 1:
        label_str += "0" * int(color_translate.get(colors[val_num]))
    label_str = format_values(int(label_str))
    if input_size in (4,5):
       label_str += f" ±{tolerance_translate.get(colors[-1])}"
    return  label_str


