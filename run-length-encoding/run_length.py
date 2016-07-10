import re


def encode(chars):
    return ''.join([str(len(match[1]) + 1) + match[0]
                    if match[1]
                    else match[0]
                    for match in re.findall(r'(.)(\1*)', chars)])


def decode(chars):
    return ''.join([int(match[0]) * match[1]
                    if match[0]
                    else match[1]
                    for match in re.findall(r'(\d*)(.)', chars)])