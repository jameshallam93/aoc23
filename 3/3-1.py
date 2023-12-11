def get_input():
    with open("3.txt", "r") as f:
        return f.readlines()


def get_neighbours(coords, lines):
    y, x = coords
    neighbours = []
    if x > 0:
        neighbours.append([y, x - 1])
        if y > 0:
            neighbours.append([y - 1, x - 1])
    if x < len(lines[y]) - 1:
        neighbours.append(
            [
                y,
                x + 1,
            ]
        )
        if y < len(lines) - 1:
            neighbours.append([y + 1, x + 1])
    if y > 0:
        neighbours.append([y - 1, x])
        if x < len(lines[y]) - 1:
            neighbours.append([y - 1, x + 1])
    if y < len(lines) - 1:
        neighbours.append([y + 1, x])
        if x > 0:
            neighbours.append([y + 1, x - 1])
    return neighbours


def get_all_neighbours(coord_range, lines):
    neighbours = []
    for coords in coord_range:
        neighbours += get_neighbours(coords, lines)
    return neighbours


def get_full_num(start, lines):
    y, x = start
    num = lines[y][x]
    end = -1
    # assumes that the number is at most 4 (3?) digits long
    for i in range(int(x) + 1, int(x) + 4):
        if i >= len(lines[y]):
            end = i
            break
        if lines[y][i].isdigit():
            num += lines[y][i]
        else:
            end = i
            break
    return num, [[y, i] for i in range(x, end)]


def is_symbol(chr):
    return chr in ["+", "-", "*", "/", "#", "&", "$", "@", "=", "%"]


def add_component_numbers(lines):
    nums = []
    for i in range(len(lines)):
        # in_last_num prevents double counting of numbers
        # e.g. 123, 23, 3.
        in_last_num = []
        for j in range(len(lines[i])):
            current = lines[i][j]
            if current.isdigit():
                # if this is a continuation of the previous number:
                if current in in_last_num:
                    in_last_num.pop(0)
                    continue
                # if this is the start of a new number:
                full_num, coord_range = get_full_num([i, j], lines)
                # add the new number's digits to in_last_num, minus first digit
                in_last_num = list(str(full_num))[1:]
                neighbours = get_all_neighbours(coord_range, lines)
                for n in neighbours:
                    if is_symbol(lines[n[0]][n[1]]):
                        nums.append(int(full_num))
                        break
    return nums


def main():
    input = get_input()
    nums = add_component_numbers(input)
    print(sum((n for n in nums)))


main()
