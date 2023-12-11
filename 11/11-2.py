def get_input():
    with open("11.txt", "r") as f:
        return [f for f in f.read().splitlines()]


def expand_space(input):
    empty_cols = [i for i in range(len(input[0])) if input[0][i] == "."]
    empty_rows = []
    for i, l in enumerate(input):
        if "#" not in l:
            empty_rows.append(i)
        else:
            non_empty_cols = [i for i in range(len(l)) if l[i] == "#"]
            for col in non_empty_cols:
                if col in empty_cols:
                    empty_cols.remove(col)
    return input, empty_rows, empty_cols


def find_shortest_path(p1, p2, empty_rows, empty_cols):
    plus_x = 0
    plus_y = 0
    for r in empty_rows:
        if r > p1[0] and r < p2[0]:
            plus_y += 1
        elif r < p1[0] and r > p2[0]:
            plus_y += 1
    for c in empty_cols:
        if c > p1[1] and c < p2[1]:
            plus_x += 1
        elif c < p1[1] and c > p2[1]:
            plus_x += 1

    y = max([p1[0], p2[0]]) - min([p1[0], p2[0]])
    x = max([p1[1], p2[1]]) - min([p1[1], p2[1]])
    return y + (999999 * plus_y) + x + (999999 * plus_x)


def get_pairs(input):
    pairs = set()
    singles = set()
    for i, l in enumerate(input):
        for j, c in enumerate(l):
            if c == "#":
                singles.add(tuple([i, j]))
    for single in singles:
        for other in singles:
            if single == other or (other, single) in pairs:
                continue
            pairs.add((single, other))
    return pairs


def sum_distances(pairs, empty_rows, empty_cols):
    sum = 0
    for p in pairs:
        sum += find_shortest_path(p[0], p[1], empty_rows, empty_cols)
    return sum


def main():
    input = get_input()
    expanded, empty_rows, empty_cols = expand_space(input)

    pairs = get_pairs(expanded)
    sum = sum_distances(pairs, empty_rows, empty_cols)
    print(sum)


main()

# 158051073243974 too high

#  449831794151 too high
#  447744640566 correct
