import numpy as np

with open("Day1/input1.txt", "r") as f:
    depth = [int(value) for value in f.readlines()]

# part1
larger_count = 0
data = [int(x) for x in depth]
for index in range(len(data) - 1):
    num1 = data[index]
    num2 = data[index + 1]
    if num2 > num1:
        larger_count += 1

print(f"Part one solution: {larger_count}")

# part2

sums_of_3 = np.array(
    [(data[i] + data[i + 1] + data[i + 2]) for i in range(len(data) - 2)]
)
diffs = np.array(sums_of_3[1:] - sums_of_3[:-1])
print(f"Part two solution: {sum(diffs > 0)}")
