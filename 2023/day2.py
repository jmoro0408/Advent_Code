import math
from pathlib import Path

input_file = Path("inputs", "day2part1.txt")

with open(input_file, "r") as f:
    data = f.readlines()



# Part 1
valid_ids = 0
for i,j in enumerate(data):
    i += 1
    games = j.split(": ")[1].strip().split(";")
    for set_ in games:
        totals = {'red':0, 'green':0, 'blue':0}
        colors_split = set_.split(", ")
        for color in colors_split:
            num, color = color.strip().split(" ")
            totals[color] = int(num)
        if totals['red'] > 12 or totals['blue'] > 14 or totals['green'] > 13:
            break
    else:
        valid_ids +=i

        
# Part 2
powers = 0
for i,j in enumerate(data):
    i += 1
    games = j.split(": ")[1].strip().split(";")
    total_totals = {'red':0, 'green':0, 'blue':0}
    
    for set_ in games:
        totals = {'red':0, 'green':0, 'blue':0}
        colors_split = set_.split(", ")
        for color in colors_split:
            num, color = color.strip().split(" ")
            totals[color] = int(num)
            if totals[color] > total_totals[color]:
                total_totals[color] = int(num)
        power = math.prod(total_totals.values())
    powers += power
print(powers)

