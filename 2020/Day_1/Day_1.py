data = open("Day_1/Data.txt").read().split()


def sum_number(number):
    sum_of_digits = 0
    for digit in str(number):
        sum_of_digits += int(digit)

    return sum_of_digits


def sum_to_2020():
    num_sums = []
    for i, number in enumerate(data):
        j = sum_number(data[i]) * sum_number(data[i - 1])
        # print(j)
        if j == 220:
            num_sums.append(number)
    if len(num_sums) == 2:
        num_sums = [int(x) for x in num_sums]
        print(num_sums[0] * num_sums[1])
        return num_sums


print(sum_number(1721))
