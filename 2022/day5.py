from utils import extract_nums, read_input
from collections import deque

INPUT_DIR = r"inputs/day5.txt"

arr = read_input(INPUT_DIR)

arr = arr.split("\n")
arr = arr[10:] #ignoring initial crates
# hardcoding input crates because parsing looks like a nightmare
crates = [
    deque('DBJV'),
    deque('PVBWRDF'),
    deque('RGFLDCWQ'),
    deque('WJPMLNDB'),
    deque('HNBPCSQ'),
    deque('RDBSNG'),
    deque('ZBPMQFSH'),
    deque('WLF'),
    deque('SVFMR'),
]

crate_dict = dict(zip(range(1,len(crates)+1), crates))
arr = [extract_nums(x) for x in arr]
arr = [[int(x) for x  in sublist] for sublist in arr]


for i in arr:
    _move = i[0] #quantity to move
    _from = i[1] #from list
    _to = i[2] #to list
    for _ in range(_move):
        moved_elem = crate_dict[_from].pop()
        crate_dict[_to].extend(moved_elem)

final_letters = []
for i in range(1,10):
    final_letters.append(crate_dict[i][-1])

print(f"Part 1: {''.join(final_letters)}")



## Part 2
arr = read_input(INPUT_DIR)

arr = arr.split("\n")
arr = arr[10:]

crates = [
    list('DBJV'),
    list('PVBWRDF'),
    list('RGFLDCWQ'),
    list('WJPMLNDB'),
    list('HNBPCSQ'),
    list('RDBSNG'),
    list('ZBPMQFSH'),
    list('WLF'),
    list('SVFMR'),
]

crate_dict = dict(zip(range(1,len(crates)+1), crates))
arr = [extract_nums(x) for x in arr]
arr = [[int(x) for x  in sublist] for sublist in arr]

for i in arr:
    _move = i[0] #quantity to move
    _from = i[1] #from list
    _to = i[2] #to list
    moved_items = crate_dict[_from][-_move:]
    crate_dict[_to].extend(moved_items)
    del crate_dict[_from][-_move:]

final_letters = []
for i in range(1,10):
    final_letters.append(crate_dict[i][-1])

print(f"Part 2: {''.join(final_letters)}")

