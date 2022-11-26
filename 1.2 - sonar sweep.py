import modules

modules.init()
data = modules.get_data("1", int)
increases = 0
for i in range(2, len(data)):
    increases += data[i] > data[i - 3]

print(increases)
