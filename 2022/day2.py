INPUT_DIR = r"inputs/day2.txt"

with open(INPUT_DIR, 'r') as f:
    arr = [line.split('\n') for line in f.readlines()]
    arr = [x[0] for x in arr]


# Part 1
scoring_dict = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }

score = 0
for pair in arr:
    score += scoring_dict[pair]

print(score)

# Part two
scoring_dict = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}


score = 0
for pair in arr:
    score += scoring_dict[pair]

print(score)