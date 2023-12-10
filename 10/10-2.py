from shapely.geometry import Point, Polygon


DIRECTION_MAP = {
    "|": [[1, 0], [-1, 0]],
    "-": [[0, 1], [0, -1]],
    "J": [[-1, 0], [0, -1]],
    "L": [[-1, 0], [0, 1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
    "S": [[-1, 0], [0, 1]],
    "O": [[-1, 0], [0, 1]],
}


def get_input():
    with open("10.txt", "r") as f:
        return [list(l.strip()) for l in f.readlines()]


def find_start(input):
    for i, l in enumerate(input):
        for j, c in enumerate(l):
            if c == "S":
                return [i, j]


def mark_loop(input, current_coords, prev_coords):
    y, x = current_coords
    current_val = input[y][x]
    possible_coords = DIRECTION_MAP[current_val]
    input[y][x] = "O"
    for p in possible_coords:
        next_coords = [y + p[0], x + p[1]]
        if next_coords == prev_coords:
            continue
        return input[next_coords[0]][next_coords[1]], next_coords


def plot_loop(input):
    start = find_start(input)
    count = 0
    prev_coords = start
    all_coords = []
    current_coords = start
    while True:
        count += 1
        next_val, next_coords = mark_loop(input, current_coords, prev_coords)
        if next_val == "O":
            break
        prev_coords = current_coords
        current_coords = next_coords
        all_coords.append(tuple(current_coords))
    return all_coords


def count_within(input, poly):
    count = 0
    for i, row in enumerate(input):
        for j, l in enumerate(row):
            if l == "O":
                continue
            if poly.contains(Point(i, j)):
                count += 1
    return count


def main():
    input = get_input()
    all_coords = plot_loop(input)
    poly = Polygon(all_coords)

    print(count_within(input, poly))


main()

# 471
