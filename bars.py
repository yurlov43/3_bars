import json
import sys
import argparse
import os.path
from math import sqrt


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8-sig") as file_json:
        return json.load(file_json)


def get_biggest_bars(bars_list):
    biggest_bar = max(
        bars_list,
        key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    biggest_bars = filter(
        lambda x: x["properties"]["Attributes"]["SeatsCount"] ==
        biggest_bar["properties"]["Attributes"]["SeatsCount"],
        bars_list)
    return biggest_bars


def get_smallest_bars(bars_list):
    smallest_bar = min(
        bars_list,
        key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    smallest_bars = filter(
        lambda x: x["properties"]["Attributes"]["SeatsCount"] ==
        smallest_bar["properties"]["Attributes"]["SeatsCount"],
        bars_list)
    return smallest_bars


def print_bars_list(print_text, bars_list):
    print(print_text)
    for bar in bars_list:
        print("{}{}".format("\t", bar["properties"]["Attributes"]["Name"]))


def get_closest_bars(bars_list, user_longitude, user_latitude):
    closest_bar = min(
        bars_list,
        key=lambda x: sqrt(
            (x["geometry"]["coordinates"][0] - user_longitude)**2 +
            (x["geometry"]["coordinates"][1] - user_latitude)**2))
    closest_bars = filter(
        lambda x: x["geometry"]["coordinates"] ==
        closest_bar["geometry"]["coordinates"],
        bars_list)
    return closest_bars


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    arg = parser.parse_args()
    if not os.path.exists(arg.filepath):
        sys.exit("Ошибка: файл не найден.")
    bars = load_data(arg.filepath)
    biggest_bars = get_biggest_bars(bars["features"])
    print_bars_list("Самые большие бары:", biggest_bars)
    smallest_bars = get_smallest_bars(bars["features"])
    print_bars_list("Самые маленькие бары:", smallest_bars)
    user_longitude = float(input('Введите долготу: '))
    user_latitude = float(input('Введите широту: '))
    closest_bars = get_closest_bars(
        bars["features"], user_longitude, user_latitude)
    print_bars_list("Самые близкие бары:", closest_bars)
