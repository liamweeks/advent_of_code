# Goal: Find the amount of calories of the elf who is carrying the most calories

import os
from os import path

BASE_DIR = os.getcwd()


def get_list_of_calories():
    return open(path.join(BASE_DIR, "calories.txt")).readlines()


def strip_calories_list(list_of_calories):
    new_list = []
    for item in list_of_calories:
        item = item.strip()
        new_list.append(item)
    return new_list


def tally_items_in_list(list):
    highest_total = 0
    current_total = 0
    current_elf = 0

    for item in list:
        current_elf += 1
        if item != '':
            current_total += int(item)
        else:  # handle occurrence of whitespaces
            if current_total > highest_total:
                highest_total = current_total
            current_total = 0
    return highest_total


print(f"Most Calories held by one elf: {tally_items_in_list(strip_calories_list(get_list_of_calories()))}")
