import re

def is_question(hey_bob):
    return hey_bob.endswith("?")
def is_yell(hey_bob):
    alpha_chars = re.sub("[^A-Za-z]","",hey_bob)
    if len(alpha_chars) == 0:
        return False
    return all(char.isupper() for char  in list(alpha_chars))
def response(hey_bob):
    hey_bob = hey_bob.strip()
    bob_response = "Whatever."
    if is_yell(hey_bob) and is_question(hey_bob):
        bob_response = "Calm down, I know what I'm doing!" 
    elif is_yell(hey_bob):
        bob_response = "Whoa, chill out!"     
    elif is_question(hey_bob):
        bob_response = "Sure."
    elif  len(hey_bob.strip()) == 0:
        bob_response = "Fine. Be that way!"
    return bob_response       