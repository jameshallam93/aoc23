import numpy as np

DIRS = [-1, 0]

TRANS = {"#": 1, ".": 0, "O": 2}

R_TRANS = {1: "#", 0: ".", 2: "O"}


def get_input():
    with open("14.txt", "r") as f:
        lines = f.readlines()
        return [list(l.strip()) for l in lines if l != ""]


def move_boulder(rocks, coords, i):
    rocks = np.array(rocks)
    di = i % 4
    rocks = np.rot90(rocks, -1 * di)
    c = coords
    r = rocks
    while True:
        if r[c[0]][c[1]] != "O":
            r = np.rot90(r, di)
            return r
        next_ = [c[0] + DIRS[0], c[1] + DIRS[1]]
        if (
            next_[0] < 0
            or next_[0] > len(r) - 1
            or next_[1] < 0
            or next_[1] > len(rocks) - 1
        ):
            r = np.rot90(r, di)
            return r
        if r[next_[0]][next_[1]] == "#":
            r = np.rot90(r, di)
            return r
        elif r[next_[0]][next_[1]] == "O":
            r = np.rot90(r, di)
            return r
        elif r[next_[0]][next_[1]] == ".":
            r[c[0]][c[1]] = "."
            r[next_[0]][next_[1]] = "O"
            c = next_


def count_rows(rocks):
    count = 0
    for i, l in enumerate(rocks):
        for c in l:
            if c == "O":
                count += len(rocks) - i
    return count


def rotate(rocks, times):
    r = np.array(rocks)
    r = np.rot90(r, times)
    return r


def get_str_rep(rocks):
    stri = ""
    i = 0
    for l in rocks:
        for r in l:
            stri += str(TRANS[r])
            i += 1

    return stri


def create_hash(rocks):
    hash = []
    for ind in range(2000):
        for i, l in enumerate(rocks):
            for j, r in enumerate(l):
                rocks = move_boulder(rocks, [i, j], ind)
        str_rep = get_str_rep(rocks)
        if ind % 4 == 3 and ind != 0:
            hash.append(str_rep)
    with open("hash.txt", "w") as f:
        for h in hash:
            f.write(h + "\n")
    return hash


def translate_hash(hash, line_len):
    rocks = []
    row = []
    hash = [int(i) for i in str(hash)]
    j = 0
    while j < len(hash):
        for i in range(line_len):
            int_rep = hash[j]
            row.append(R_TRANS[int_rep])
            j += 1
        rocks.append(row)
        row = []
    return rocks


def find_repeating(hash):
    max_ = int(len(hash)) - 1
    min_ = 30
    poss = []
    for i in range(min_, max_):
        j = 0
        while j < int(len(hash)) - (min_ * 2):
            comp_1 = hash[j : j + i]
            comp_2 = hash[j + i : j + (i * 2)]
            if comp_1 == comp_2:
                poss.append([j, i])
                j += i
            else:
                j += 1
    return poss[0]


def get_hash_from_file():
    with open("hash.txt", "r") as f:
        return [l.replace("\n", "") for l in f.readlines()]


def main():
    rocks = get_input()
    l = len(rocks[0])
    hash = create_hash(rocks)
    # uncomment below after first run to avoid having to recreate hash each time
    # HASH = get_hash_from_file()
    start, length = find_repeating(hash)
    pattern = hash[start : start + length]
    i = (1000000000 - (start + 1)) % (length)
    print(count_rows(translate_hash(pattern[i], l)))


main()

# 103445
