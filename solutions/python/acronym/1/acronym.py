from string import punctuation
import re

PUNCTUATION_NO_DASH_REGEX  = f"[{re.escape(punctuation.replace('-',''))}]"


def abbreviate(words):
    words = re.sub(PUNCTUATION_NO_DASH_REGEX,"", words)
    words = words.replace("-", " ")
    words = re.sub(r"\s+", " ", words)
    word_list = words.split(" ")
    return "".join([word[0].upper() for word in word_list])
    
