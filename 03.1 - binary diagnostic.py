from modules import DataManager
from typing import List

data = DataManager(__file__).get_data_string()

compareList: List[float] = []
gamma = "0b"
epsilon = "0b"

for i in range(0, len(data[0])):
    compareList.append(-len(data) / 2)
    for val in data:
        compareList[i] += float(val[i])
    if compareList[i] > 0:
        gamma += "1"
        epsilon += "0"
        continue
    if compareList[i] == 0:
        print(f"Equal amount of 0 and 1 in position {i}.")
    gamma += "0"
    epsilon += "1"

print(int(gamma, 2) * int(epsilon, 2))
