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


def find_reflection_point(reflection, axis, p, target_occs=0):
    p0, p1 = p
    occurrences = 0
    if axis == "x":
        if p1 > len(reflection) - 1:
            return False
        to_compare = list(reversed(reflection[: p0 + 1])), reflection[p1:]
        for i in range(min([len(to_compare[0]), len(to_compare[1])])):
            if to_compare[0][i] != to_compare[1][i]:
                for j, char in enumerate(to_compare[0][i]):
                    if char != to_compare[1][i][j]:
                        occurrences += 1
                if occurrences > target_occs:
                    return False

        return p1 if occurrences == target_occs else False

    if axis == "y":
        if p1 > len(reflection[0]) - 1:
            return False
        to_compare = []
        columns = [
            [reflection[i][j] for i in range(len(reflection))]
            for j in range(len(reflection[0]))
        ]
        to_compare = list(reversed(columns[: p0 + 1])), columns[p1:]
        for i in range(min([len(to_compare[0]), len(to_compare[1])])):
            if to_compare[0][i] != to_compare[1][i]:
                for j, char in enumerate(to_compare[0][i]):
                    if char != to_compare[1][i][j]:
                        occurrences += 1
                if occurrences > target_occs:
                    return False
        return p1 if occurrences == target_occs else False


def summarize_reflection_lines(reflections, target_occurrences):
    sum = 0    
    for r in reflections:
        reflection_point = False
        for i in range(0, len(r)):
            reflection_point = find_reflection_point(
                r, "x", (i, i + 1), target_occs=target_occurrences
            )
            if reflection_point:
                sum += reflection_point * 100
                break
        if not reflection_point:
            for j in range(0, len(r[0])):
                reflection_point = find_reflection_point(
                    r, "y", (j, j + 1), target_occs=target_occurrences
                )
                if reflection_point:
                    sum += reflection_point
                    break
        if not reflection_point:
            print("no reflection point found for reflection: ")
            print(r)
            return False
    return sum


def main():
    # set to 0 for part 1, 1 for part 2
    target_occurrences = 0
    input = get_input()
    reflections = format_reflections(input)
    print(summarize_reflection_lines(reflections, target_occurrences))


main()

# 31877 pt 1
# 42996 pt 2
