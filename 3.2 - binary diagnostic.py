import modules
from typing import List


def filter_most_common(unfiltered: List[str], index: int) -> List[str]:
    common = most_common_1([word[index] for word in unfiltered])
    return list(filter(lambda item: item[index] == common, unfiltered))


def filter_least_common(unfiltered: List[str], index: int) -> List[str]:
    common = most_common_1([word[index] for word in unfiltered])
    return list(filter(lambda item: item[index] != common, unfiltered))


def most_common_1(binary_list: List[str]) -> str:
    ones = binary_list.count("1")
    length = len(binary_list)
    if ones >= length / 2:
        val = "1"
    else:
        val = "0"
    print(f"{val} is most common: {ones}/{length} are \"1\"")
    return val


modules.init()
data = modules.get_data_string("3")

oxygen_candidates = data.copy()
co2_candidates = data.copy()

print("Figuring out the oxygen generator rating:")
for i in range(0, len(data[0])):
    oxygen_candidates = filter_most_common(oxygen_candidates, i)
    if len(oxygen_candidates) == 1:
        oxygen_bin = oxygen_candidates[0]
        oxygen = int(oxygen_bin, 2)
        break

print(f"oxygen generator rating: {oxygen} / {oxygen_bin}")

print("Figuring out the co2 scrubber rating:")
for i in range(0, len(data[0])):
    co2_candidates = filter_least_common(co2_candidates, i)
    if len(co2_candidates) == 1:
        co2_bin = co2_candidates[0]
        co2 = int(co2_bin, 2)
        break

print(f"co2 scrubber rating: {co2} / {co2_bin}")

print(oxygen * co2)
