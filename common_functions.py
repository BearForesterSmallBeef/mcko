def get_space_ships_data(path: str) -> list:
    with open(path, "r", encoding="utf-8") as read_file:
        data = list(map(lambda x: x.split("*"), read_file.readlines()[1:]))
        read_file.close()
    for element in data:
        element[2] = list(map(int, element[2].split()))
        element[3] = list(map(int, element[3].split()))
        element[0] = list(element[0].split("-"))
    return data


def write_data_to_file(path: str, data: list, separator="*", lenght=4) -> bool:
    try:
        for position, element in enumerate(data):
            element = element[:lenght]
            element[0] = "-".join(element[0])
            element[2] = " ".join(list(map(str, element[2])))
            element[3] = " ".join(list(map(str, element[3])))
            data[position] = element
        data = ["ShipName*planet*coord_place*direction"] + list(map(lambda x: "\n" + separator.join(x), data))

        with open(path, "w", encoding="utf-8") as write_file:
            write_file.writelines(data)
            write_file.close()
        return True
    except Exception as exception:
        print(exception)
        return False
