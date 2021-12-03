from collections import Counter


def frequent(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]


with open("day3/input3.txt", "r") as f:
    data = f.readlines()
    data = [(line.rstrip()) for line in data]
    count = {k: [] for k in range(len(data[0]))}
    most_common_bin = {k: 0 for k in range(len(data[0]))}
    for j, num in enumerate(data):
        for index, value in enumerate(num):
            count[index].append(value)
            most_common_bin[index] = frequent(count[index])

    gamma_bin = "".join([str(value) for value in most_common_bin.values()])
    epsilon_bin = "".join("1" if x == "0" else "0" for x in gamma_bin)
    gamma = int(gamma_bin, 2)
    epsilon = int(epsilon_bin, 2)

    power_consumption = gamma * epsilon

    print(f"Power consumption: {power_consumption}")
