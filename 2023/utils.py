import re


def extract_numbers(input_string):
    numbers = re.findall(r'\b\d+\b', input_string)
    return numbers