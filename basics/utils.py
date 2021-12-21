import re


def sanitize_number(string):
    value = re.findall(r'[0-9]+', string)
    return ''.join(value)

