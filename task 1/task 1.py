from common_functions import *


input_path = "C:\\Users\\MLess\\PycharmProjects\\mcko\\space.txt"
output_path = "answer_task_1.txt"

data = get_space_ships_data(input_path)

for ship in data:
    if ship[2] == [0, 0]:
        n = int(ship[0][1][0])
        m = int(ship[0][1][1])
        t = len(ship[0][0])
        xd, yd = ship[3]

        if n > 5:
            x = n + xd
        else:
            x = (n + xd) * (-4) + t

        if m > 3:
            y = m + t + yd
        else:
            y = -(n + yd) * m

        ship[2] = [x, y]
    if ship[0][0][-1] == "V":
        ship_name = '-'.join(ship[0])
        x, y = ship[2]
        print(f"{ship_name} - ({x}, {y})")

write_data_to_file(output_path, data)
