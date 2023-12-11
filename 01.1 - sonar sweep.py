from modules import DataManager

data = DataManager(__file__).get_data(int)

last = False
increases = 0
for val in data:
    if last:
        increases += val > last
    last = val

print(increases)
