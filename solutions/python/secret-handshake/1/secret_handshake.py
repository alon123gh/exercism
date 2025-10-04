def commands(binary_str):
    hand_shake = []
    code = int(binary_str,2)
    actions = [(0b00001, "wink" ) , (0b00010, "double blink" ),(0b00100 , "close your eyes" ), (0b01000, "jump" ) ]
    for action_code, action_name in actions:
        if code & action_code != 0 :
            hand_shake.append(action_name)
    if code & 0b10000 :
        hand_shake.reverse()        
    return hand_shake
  
