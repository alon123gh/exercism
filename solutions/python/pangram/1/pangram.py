def is_pangram(sentence):
    sentence = "".join(ch for ch in sentence if ch.isalpha())
    all_letters = set(list("abcdefghijklmnopqrstuvwxyz"))
    return set(list(sentence.lower())) == all_letters
