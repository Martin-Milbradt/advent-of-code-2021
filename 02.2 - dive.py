from modules import DataManager

data = DataManager(__file__).get_data_string()

forward = 0
depth = 0
aim = 0

for command in data:
    direction, distance = command.split(" ")
    match direction:
        case "forward":
            forward += int(distance)
            depth += aim * int(distance)
        case "down":
            aim += int(distance)
        case "up":
            aim -= int(distance)
        case _:
            print(f"Error, direction {direction} unknown")

print(depth * forward)
