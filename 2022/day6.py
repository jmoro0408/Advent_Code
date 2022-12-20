from utils import read_input

INPUT_DIR = r"inputs/day6.txt"

arr = read_input(INPUT_DIR)


a=list(arr[:4])

for i in range(4,len(arr)):
    if len(set(a))==4:print(i);break
    a.pop(0)
    a.append(arr[i])

## Part two
a=list(arr[:14])
for i in range(14,len(arr)):
    if len(set(a))==14:print(i);break
    a.pop(0)
    a.append(arr[i])
