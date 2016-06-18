import re
# Wordcount: count the occurrences of each word in that phrase.
def word_count(phrase):
    phrase = re.sub(r'\W+|_', ' ', phrase.lower(), flags=re.UNICODE)
    word_list = phrase.split()
    wordfreq = [word_list.count(p) for p in word_list]
    return dict(zip(word_list, wordfreq))
