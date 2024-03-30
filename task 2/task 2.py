from common_functions import *


input_path = "C:\\Users\\MLess\\PycharmProjects\\mcko\\task 1\\answer_task_1.txt"
output_path = "answer_task_2.txt"

data = get_space_ships_data(input_path)

lenght = len(data)
for i in range(lenght):
    for j in range(0, lenght - i - 1):
        if int(data[j][0][1]) > int(data[j + 1][0][1]):
            data[j], data[j + 1] = data[j + 1], data[j]

for ship in data[:10]:
    print('-'.join(ship[0]))

write_data_to_file(output_path, data)
