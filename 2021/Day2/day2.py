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

print(f"final position: {position}")
print(f"final result: {position[0] * position[1]}")
