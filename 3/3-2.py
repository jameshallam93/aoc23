def get_input():
    with open("three.txt", "r") as f:
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


def get_full_num(coord, lines):
    y, x = coord
    y, x = int(y), int(x)
    num = lines[y][x]

    # start at x + 1, go right until you hit a non-digit or end of line
    for i in range(x + 1, x + 3):
        if i >= len(lines[y]):
            break
        if lines[y][i].isdigit():
            # append to end of num
            num += lines[y][i]
        else:
            break
    # start at x-1, go left until you hit a non-digit or start of line
    for i in range(x - 1, x - 3, -1):
        if i < 0:
            break
        if lines[y][i].isdigit():
            # add to start of num
            num = lines[y][i] + num
        else:
            break
    return num


def get_num_neighbours(coords, lines):
    neighbours = get_neighbours(coords, lines)
    num_neighbours = set()
    for neighbour in neighbours:
        y, x = neighbour
        if lines[y][x].isdigit():
            # this would be bad if there were two equal numbers around one gear
            # should really add coord ranges to a list of 'registered_nums'
            # rather than relying on a set
            num_neighbours.add(get_full_num(neighbour, lines))
    return num_neighbours


def find_gears(lines):
    gears = []
    for y, line in enumerate(lines):
        for x, chr in enumerate(line):
            if chr == "*":
                num_neighbours = get_num_neighbours([y, x], lines)
                if len(num_neighbours) == 2:
                    gears.append(num_neighbours)
    return gears


def get_ratios(gears):
    sum = 0
    for g in gears:
        sum += int(g.pop()) * int(g.pop())
    return sum


def main():
    input = get_input()
    gears = find_gears(input)
    print(get_ratios(gears))


main()
