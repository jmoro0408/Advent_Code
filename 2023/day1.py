import re
from pathlib import Path

input_file = Path('inputs', 'day1part1.txt')

with open(input_file, 'r') as f:
    data = f.readlines()

def part1():
    def get_digits(string):
        digits = [x for x in string if x.isdigit()]
        if len(digits) == 1:
            return int(digits[0] + digits[0])
        return int(digits[0] + digits[-1])

    print(sum(get_digits(x) for x in data))
    

import re

t = 0
number_words = "one two three four five six seven eight nine".split()
pattern = "(?=(" + "|".join(number_words) + "|\\d))"

def convert_to_digit(word):
    if word in number_words:
        return str(number_words.index(word) + 1)
    return word

for string_data in data:
    digits = [*map(convert_to_digit, re.findall(pattern, string_data))]
    t += int(digits[0] + digits[-1])

print(t)
