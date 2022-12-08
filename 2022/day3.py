import string
import itertools
INPUT_DIR = r"inputs/day3.txt"

with open(INPUT_DIR, "r") as f:
    arr = [line.split("\n") for line in f.readlines()]
    arr = [x[0] for x in arr]

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
values = range(1,53)
priority_dict = dict(zip(letters,values))

# Part 1

common_items_list = []
for rucksack in arr:
    compartment_1 = set(rucksack[: int(len(rucksack) / 2)])
    compartment_2 = set(rucksack[int(len(rucksack) / 2):])
    common_items = compartment_1.intersection(compartment_2)
    common_items_list.append(common_items)

common_items_list = [item for sublist in common_items_list for item in sublist]

priority_sum = 0
for item in common_items_list:
    priority_sum += priority_dict[item]

# print(priority_sum)

## Part 2

common_items = []
ii = 0
while ii < len(arr):
    bag1 = arr[ii]
    bag2 = arr[ii+1]
    bag3 = arr[ii+2]
    for item in bag1:
        if (item in bag2) and (item in bag3):
            common_items.append(item)
            ii += 3
            break

priority_sum = 0
for item in common_items:
    priority_sum += priority_dict[item]

print(priority_sum)
