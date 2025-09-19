import re

def translate(text):
    
    """
    Translate a phrase or sentence from English to Pig Latin.

    The function splits the input string into words, applies Pig Latin rules
    to each word, and then joins the results back into a single string.

    Rules implemented
    -----------------
    - If a word begins with a vowel sound (``a``, ``e``, ``i``, ``o``, ``u``),
      or with the clusters ``xr`` or ``yt``, append ``"ay"`` to the end.
    - If a word starts with one or more consonants followed by ``qu``,
      move the leading consonants plus ``qu`` to the end, then append ``"ay"``.
    - If a word contains ``y`` after one or more consonants,
      treat the ``y`` as the start of the word: move everything before ``y`` to the end,
      then append ``"ay"``.
    - Otherwise, for a word beginning with one or more consonants,
      move the initial consonant(s) to the end and append ``"ay"``.

    Parameters
    ----------
    text : str
        A string containing one or more space-separated words to translate.

    Returns
    -------
    str
        The input phrase translated into Pig Latin, with word order preserved.

    Notes
    -----
    - The function assumes input is lowercase and contains no punctuation.
    - Words are split on spaces only; punctuation handling must be added separately.
    """

    words = text.split()
    translated_words = []
    for word in words:
        if re.match("^([aeiou]|xr|yt)", word): 
            word  += "ay"
        elif m := re.match(r"^([^aeiou]*?qu)(.*)", word):     
             word = m.group(2) +  m.group(1) + "ay"               
        elif m := re.match("^([^aeiou]+)y(.*)", word):     
             word = "y" + m.group(2) + m.group(1) + "ay"        
        elif m := re.match("^([^aeiou]+)(.*)", word):    
            word = m.group(2) + m.group(1) + "ay"
        translated_words.append(word)
    return " ".join(translated_words)
       
    return text