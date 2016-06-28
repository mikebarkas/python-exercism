#
# Skeleton file for the Python "Bob" exercise.
#


def hey(prompt):
    test = not prompt.strip(), prompt.isupper(), prompt.endswith('?'), prompt.endswith(' '), True
    reply = 'Fine. Be that way!', 'Whoa, chill out!', 'Sure.', 'Sure.', 'Whatever.'
    return reply[test.index(True)]
