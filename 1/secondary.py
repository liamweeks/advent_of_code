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


def combine_calorie_components(stripped_list_of_calories):
    list_of_total_calories_per_elf = []
    current_total = 0

    for i in stripped_list_of_calories:
        if not i == '':
            current_total += int(i)
        else:
            list_of_total_calories_per_elf.append(current_total)
            current_total = 0
    return list_of_total_calories_per_elf



def get_n_largest_amounts_of_calories(stripped_list, n):
    stripped_list.sort(reverse=True)
    total_calories = 0

    for i in range(0, n):
        total_calories += stripped_list[i]
    return total_calories




if __name__ == "__main__":
    unorganized_data = get_list_of_calories()
    stripped_list = strip_calories_list(unorganized_data)
    summed_totals_per_elf = combine_calorie_components(stripped_list)
    top_3 = get_n_largest_amounts_of_calories(summed_totals_per_elf, 3)

    print(f"Total amount of calories carried by the top 3 elves: {top_3}")
