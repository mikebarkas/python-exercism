# Hamming distance.
def distance(strand_one, strand_two):
    try:
        assert len(strand_one) == len(strand_two)
    except AssertionError:
        return 'The strings must be equal length.'

    return sum(char1 != char2 for char1, char2 in zip(strand_one, strand_two))
