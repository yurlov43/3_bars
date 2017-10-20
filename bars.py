import json
import sys
import os.path
from math import sqrt


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8-sig") as file_json:
        return json.load(file_json)


def get_biggest_bar(bars):
    biggest_bar = max(
        bars["features"],
        key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    biggest_bars = filter(
        lambda x: x["properties"]["Attributes"]["SeatsCount"] ==
        biggest_bar["properties"]["Attributes"]["SeatsCount"],
        bars["features"])
    return biggest_bars


def get_smallest_bar(bars):
    smallest_bar = min(
        bars["features"],
        key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    smallest_bars = filter(
        lambda x: x["properties"]["Attributes"]["SeatsCount"] ==
        smallest_bar["properties"]["Attributes"]["SeatsCount"],
        bars["features"])
    return smallest_bars


def print_list_bar(str, bars):
    print(str)
    for bar in bars:
        print("\t" + bar["properties"]["Attributes"]["Name"])


def get_closest_bar(bars, longitude, latitude):
    closest_bar = min(
        bars["features"],
        key=lambda x: sqrt(
            (x["geometry"]["coordinates"][0] - longitude)**2 +
            (x["geometry"]["coordinates"][1] - latitude)**2))
    closest_bars = filter(
        lambda x: x["geometry"]["coordinates"] ==
        closest_bar["geometry"]["coordinates"],
        bars["features"])
    return closest_bars


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Ошибка: не указан файл.")
    if len(sys.argv) > 2:
        sys.exit("Ошибка: слишком много параметров.")
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        sys.exit("Ошибка: файл не найден.")
    bars = load_data(filepath)
    biggest_bars = get_biggest_bar(bars)
    print_list_bar("Самые большие бары:", biggest_bars)
    smallest_bars = get_smallest_bar(bars)
    print_list_bar("Самые маленькие бары:", smallest_bars)
    longitude = float(input('Введите долготу (начиная с 37.): '))
    latitude = float(input('Введите широту (начиная с 55.): '))
    closest_bars = get_closest_bar(bars, longitude, latitude)
    print_list_bar("Самые близкие бары:", closest_bars)
