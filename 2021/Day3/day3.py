import numpy as np
import pandas as pd

data = np.genfromtxt("Day3/input3.csv", dtype=str)
data_df = pd.DataFrame(data=[list(i) for i in data])

bin_num = data_df.mode().sum().sum()
gamma = int(bin_num, 2)
inverted_bin = "".join("1" if x == "0" else "0" for x in bin_num)
epsilon = int(inverted_bin, 2)

power_consumption = gamma * epsilon

print(f"Power consumption: {power_consumption}")

# Part2
oxy_df = data_df.copy()
co2_df = data_df.copy()

for value in oxy_df.columns:
    most_common = oxy_df[value].mode()
    if len(most_common) > 1:
        oxy_df = oxy_df[oxy_df[value].values == "1"]
    else:
        oxy_df = oxy_df[oxy_df[value].values == most_common.iloc[0]]
    if len(oxy_df) == 1:
        ox = int(oxy_df.iloc[0].sum(), 2)
        break

for value in co2_df.columns:
    mode = co2_df[value].mode()
    if len(mode) > 1:
        co2_df = co2_df[co2_df[value].values == "0"]
    else:
        co2_df = co2_df[co2_df[value].values == str(1 - int(mode.iloc[0]))]
    if len(co2_df) == 1:
        CO2 = int(co2_df.iloc[0].sum(), 2)
        break

print(f"Lift support rating: {ox * CO2}")
