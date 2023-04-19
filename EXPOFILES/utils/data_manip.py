import re


def list_to_string(day_list: list[str]):
    str_list = ""

    for index, day in enumerate(day_list):
        if index == 0:
            str_list += day
        elif index == 3:
            str_list += f"\n{day}"
        else:
            str_list += f", {day}"
    return str_list


def string_to_list(string):
    my_list = re.split(r"[,|\n]", string)
    formatted_list = [item.strip() for item in my_list]
    return formatted_list
