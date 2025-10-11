from string import ascii_lowercase
from string import digits

ENCODER = dict(zip(ascii_lowercase+digits, "".join(reversed(ascii_lowercase)) + digits ))
DECODER = dict(zip("".join(reversed(ascii_lowercase)) + digits ,ascii_lowercase + digits))
GROUP_SIZE = 5
  
def encode(plain_text):
    plain_text = plain_text.lower()
    text = ""
    for idx in range(0,len(plain_text)):
         ch = plain_text[idx]
         text += ENCODER.get(ch,"")       
    return " ".join([text[pos:pos+GROUP_SIZE] for pos in range(0,len(text), GROUP_SIZE )])

def decode(ciphered_text):
    text = ""
    ciphered_text = ciphered_text.replace(" ","")
    for idx in range(0,len(ciphered_text)):
        ch = ciphered_text[idx]
        text += DECODER.get(ch,ch)       
    return text
