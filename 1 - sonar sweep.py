import modules

modules.init()
data = modules.get_data_string("1")
last = False
increases = 0
for val in data:
    if last:
        increases += val > last
        if val <= last:
            print(f"val - last = {val - last}")
    last = val

print(increases)
