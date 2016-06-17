# Wordcount: count the occurrences of each word in that phrase.
def word_count(phrase):
    word_list = phrase.lower().split()
    wordfreq = [word_list.count(p) for p in word_list]

    return dict(zip(word_list, wordfreq))
