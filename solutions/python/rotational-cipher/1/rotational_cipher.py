from string import ascii_lowercase
from string import ascii_uppercase

def rotate(text, key):

    ALL_CHAR_LEN = 26    
    key = key % ALL_CHAR_LEN
    rotated_cipher_string_lower = ascii_lowercase[key:] + ascii_lowercase[:key] 
    rotated_cipher_string_upper = ascii_uppercase[key:] + ascii_uppercase[:key] 
    chiper = dict(zip(ascii_lowercase + ascii_uppercase, rotated_cipher_string_lower+rotated_cipher_string_upper))
    return "".join([chiper.get(ch,ch) for ch in list(text) ])
  
