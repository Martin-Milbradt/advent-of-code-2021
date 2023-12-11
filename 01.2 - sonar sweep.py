from modules import DataManager

data = DataManager(__file__).get_data(int)

increases = 0
for i in range(2, len(data)):
    increases += data[i] > data[i - 3]

print(increases)
