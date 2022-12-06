INPUT_DIR = r"inputs/day1.txt"

with open(INPUT_DIR, 'r') as f:
    arr = [line.split('\n') for line in f.readlines()]
    arr = [x[0] for x in arr]

ll = []
l = []

for i in arr:
    if i != '':
        l.append(int(i))
    else:
        ll.append(l)
        l = []
        continue

# Part 1
sums_list = [sum(i) for i in ll]
print(max(sums_list))

# Part 2

print(sum(sorted(sums_list, reverse = True)[:3]))

