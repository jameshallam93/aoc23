

def get_input():
    with open("11-test.txt", "r") as f:
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

    for row in reversed(empty_rows):
        input.insert(row+1, "." * len(input[0]))
    for col in reversed(empty_cols):
        for i, l in enumerate(input):
            input[i] = l[:col] + "." + l[col:]
    return input

def find_shortest_path(p1, p2):
    y = max([p1[0], p2[0]]) - min([p1[0], p2[0]])
    x = max([p1[1], p2[1]]) - min([p1[1], p2[1]])
    return y + x

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

def sum_distances(pairs):
    sum = 0
    for p in pairs:
        sum += find_shortest_path(p[0], p[1])
    return sum  

def main():
    input = get_input()
    expanded = expand_space(input)

    pairs = get_pairs(expanded)
    sum = sum_distances(pairs)
    print(sum)

main()

# 19072076 too high
# 9536038 correct