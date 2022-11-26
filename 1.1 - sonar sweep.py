import modules

modules.init()
data = modules.get_data("1", int)
last = False
increases = 0
for val in data:
    if last:
        increases += val > last
    last = val

print(increases)
