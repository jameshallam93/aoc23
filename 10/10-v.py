import matplotlib.pyplot as plt
import numpy as np
import time
import os

DIRECTION_MAP = {
    "|": [[1, 0], [-1, 0]],
    "-": [[0, 1], [0, -1]],
    "J": [[-1, 0], [0, -1]],
    "L": [[-1, 0], [0, 1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
    "S": [[-1, 0], [0, 1]],
}
SYMBOL_MAP = {
    "|": "|",
    "-": "-",
    "J": "┛",
    "L": "┗",
    "7": "┓",
    "F": "┏",
    "S": "┗",
    ".": " "
}


def get_input():
    with open("10.txt", "r") as f:
        return [l.strip() for l in f.readlines()]

def find_start(input):
    for i, l in enumerate(input):
        for j, c in enumerate(l):
            if c == "S":
                return [i, j]


def get_next(input, current_coords, prev_coords):
    y, x = current_coords
    current_val = input[y][x]
    possibles = DIRECTION_MAP[current_val]
    for pos in possibles:
        next_coords = [y + pos[0], x + pos[1]]
        if next_coords == prev_coords:
            continue
        return input[next_coords[0]][next_coords[1]], next_coords


def print_slice(input, current_coords, prev_list):
    PREV_COLOR = '\033[92m'
    END_C = '\033[0m'
    upper_y, lower_y = current_coords[0] - 20, current_coords[0] + 20
    upper_x, lower_x = current_coords[1] - 40, current_coords[1] + 40
    if upper_y < 0:
        lower_y -= upper_y
        upper_y = 0
    if upper_x < 0:
        lower_x -= upper_x
        upper_x = 0
    if lower_y > len(input):
        upper_y += len(input) - lower_y
        lower_y = len(input)
    if lower_x > len(input[0]):
        upper_x += len(input[0]) - lower_x
        lower_x = len(input[0])
    slice = [list(r) for r in input[upper_y:lower_y]]
    for i, l in enumerate(slice):
        slice[i] = l[upper_x:lower_x]
    for i, l in enumerate(slice):
        for j, c in enumerate(l):
            if [i + upper_y, j + upper_x] in prev_list:
                slice[i][j] = f"{PREV_COLOR}{c}{END_C}"
    os.system("clear")
    for l in slice:
        print("".join(l))
    print("\n")
    time.sleep(0.1)


def get_furthest(input, symbols):
    start = find_start(input)
    count = 0
    prev = start
    prev_list = [start]
    current_coords = start
    while True:
        print_slice(symbols, current_coords, prev_list)
        count += 1
        next_val, next_coords = get_next(input, current_coords, prev)
        if next_val == "S":
            return count / 2
        prev = current_coords
        current_coords = next_coords
        prev_list.append(current_coords)

def find_start(input):
    for i, l in enumerate(input):
        for j, c in enumerate(l):
            if c == "S":
                return [i, j]

def main():
    input = get_input()
    symbol_representation = [[SYMBOL_MAP[c] for c in l] for l in input]
    print_slice(symbol_representation, find_start(input), [find_start(input)])
    time.sleep(0.5)
    get_furthest(input, symbol_representation)

main()