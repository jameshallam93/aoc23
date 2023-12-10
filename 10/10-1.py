DIRECTION_MAP = {
    "|": [[1, 0], [-1, 0]],
    "-": [[0, 1], [0, -1]],
    "J": [[-1, 0], [0, -1]],
    "L": [[-1, 0], [0, 1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
    "S": [[-1, 0], [0, 1]],
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


def get_furthest(input):
    start = find_start(input)
    count = 0
    prev = start
    current_coords = start
    while True:
        count += 1
        next_val, next_coords = get_next(input, current_coords, prev)
        if next_val == "S":
            return count / 2
        prev = current_coords
        current_coords = next_coords


def main():
    input = get_input()
    print(get_furthest(input))


main()

# 6875
