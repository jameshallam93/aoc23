def get_input():
    with open("nine.txt", "r") as f:
        return f.read().splitlines()


def get_next_line(line):
    next_ = []
    for i, n in enumerate(line):
        if i == len(line) - 1:
            return next_
        next_.append(int(line[i + 1]) - int(n))


def extrapolate(line):
    """
    "1 3 6 10 15"
    =>
    [
        [1, 3, 6, 10, 15],
        [2, 3, 4, 5],
        [1, 1, 1],
        [0, 0]
    ]
    """
    l = line.split(" ")
    lines = [[int(i) for i in l]]
    while not all([n == 0 for n in l]):
        l = get_next_line(l)
        lines.append(l)
    return lines


def expand_line(line):
    prev = 0
    for l in reversed(line):
        l.append(prev + l[-1])
        prev = l[-1]
    return line


def sum_expanded(expanded):
    sum = 0
    for e in expanded:
        sum += e[0][-1]
    return sum


def main():
    input = get_input()
    extrapolated = [extrapolate(l) for l in input]
    expanded = [expand_line(l) for l in extrapolated]
    total = sum_expanded(expanded)
    print(total)


main()

# 1782868781
