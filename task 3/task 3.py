from common_functions import *


input_path = "C:\\Users\\MLess\\PycharmProjects\\mcko\\task 2\\answer_task_2.txt"

data = get_space_ships_data(input_path)

ship_dict = dict()
for ship in data:
    ship_dict['-'.join(ship[0])] = ship
while True:
    ship_name = input().strip()
    if ship_name == "stop":
        break
    if ship_name not in ship_dict.keys():
        print("error.. er.. ror..")
    else:
        ship = ship_dict[ship_name]
        direction = " ".join(list(map(str, ship[3])))
        print(f"Корабль {ship_name} был отправлен с планеты: {ship[1]} и его направление движения было: {direction}")
