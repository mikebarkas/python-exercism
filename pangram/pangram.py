from string import ascii_lowercase


# Pangram.
def is_pangram(phrase):
    return set(ascii_lowercase).issubset(set(phrase.lower()))
