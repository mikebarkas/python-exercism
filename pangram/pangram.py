# Pangram.
def is_pangram(phrase):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Filter user input.
    string = phrase.lower()
    string = string.replace('"', '').replace('.', '')

    for letter in alphabet:
        if not letter in string:
           return False
    return True
