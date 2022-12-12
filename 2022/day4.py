INPUT_DIR = r"inputs/day4.txt"

with open(INPUT_DIR) as f:
    arr = f.read().strip()

arr = arr.split("\n")

print(arr)

# PArt 1
c = 0
for i in arr:
    a,b = i.split(",")
    a1, a2 = map(int,a.split("-"))
    b1, b2 = map(int,b.split("-"))
    if (a1<=b1 <=b2<=a2) or (b1<=a1<=a2<=b2):
        c+=1
print(c)

# Part 2
c = 0
for i in arr:
    a,b = i.split(",")
    a1, a2 = map(int,a.split("-"))
    b1, b2 = map(int,b.split("-"))
    if a2 >= b1 and a1 <=b2 or b2 >=a1 and b1 <= a2:
        c+=1
print(c)
