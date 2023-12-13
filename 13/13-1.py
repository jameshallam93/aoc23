def get_input():
    with open("13.txt", "r") as f:
        return [l for l in f.read().splitlines()]


def format_reflections(input):
    reflections = []
    c = []
    for i in input:
        if i == "":
            reflections.append(c)
            c = []
        else:
            c.append(i)
    reflections.append(c)
    return reflections


def find_reflection_point(reflection, axis, p):
    p0, p1 = p
    if axis == "x":
        if p1 > len(reflection) - 1:
            return False
        to_compare = list(reversed(reflection[: p0 + 1])), reflection[p1:]
        for i in range(len(min(to_compare))):
            if to_compare[0][i] != to_compare[1][i]:
                return False

        return p0 + 1

    if axis == "y":
        if p1 > len(reflection[0]) - 1:
            return False
        to_compare = []
        i = 0
        columns = [
            [reflection[i][j] for i in range(len(reflection))]
            for j in range(len(reflection[0]))
        ]
        to_compare = list(reversed(columns[: p0 + 1])), columns[p1:]
        for i in range(len(min(to_compare))):
            if to_compare[0][i] != to_compare[1][i]:
                return False
        return p0 + 1


def main():
    input = get_input()
    reflections = format_reflections(input)
    sum = 0
    for r in reflections:
        reflection_point = False
        for i in range(0, len(r)):
            reflection_point = find_reflection_point(r, "x", (i, i + 1))
            if reflection_point:
                sum += reflection_point * 100
                break
        if not reflection_point:
            for j in range(0, len(r[0])):
                reflection_point = find_reflection_point(r, "y", (j, j + 1))
                if reflection_point:
                    sum += reflection_point
                    break
        if not reflection_point:
            print("no reflection point found")
            return False
    print(sum)


main()


# 31877
