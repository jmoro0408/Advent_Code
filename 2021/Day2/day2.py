with open("day2/input2.txt", "r") as f:
    dive = f.readlines()
    dive = [line.rstrip() for line in dive]

# part1
position = [0, 0]  # x,y

for line in dive:
    space_index = line.index(" ")
    direction = line[:space_index]
    magnitude = int(line[space_index:])
    if direction == "forward":
        position[0] += magnitude
    elif direction == "down":
        position[1] += magnitude
    elif direction == "up":
        position[1] -= magnitude

print(f"Part 1 final position: {position}")
print(f"Part 1 final result: {position[0] * position[1]}")


# part2
position = [0, 0, 0]  # horizontal, depth, aim
for line in dive:
    space_index = line.index(" ")
    direction = line[:space_index]
    magnitude = int(line[space_index:])
    if direction == "forward":
        position[0] += magnitude
        position[1] += position[2] * magnitude
    elif direction == "down":
        position[2] += magnitude
    elif direction == "up":
        position[2] -= magnitude

print(f"Part 2 final position: {position}")
print(f"Part 2 final result: {position[0] * position[1]}")
