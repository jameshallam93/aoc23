import itertools
from copy import deepcopy
from functools import cache


def get_input():
    with open("12.txt", "r") as f:
        return [l.strip().split(" ") for l in f.readlines() if l != ""]


def get_springs(row, five_times=False):
    springs, setup = row
    if five_times:
        springs = list("?".join(5 * [springs]))
        setup = [int(s) for s in setup.split(",")]
        setup = setup * 5
    else:
        springs = list(springs)
        setup = [int(s) for s in setup.split(",")]
    return springs, setup


@cache
def count_(springs, specs, current_group, spec_index=0, force_skip=False):
    # this is a travesty
    springs_ = deepcopy(list(springs))
    specs = list(specs)
    current_group = list(current_group)
    try:
        current = springs_.pop(0)
    except Exception:
        if spec_index >= len(specs):
            return 1
        if len(current_group) == specs[spec_index]:
            return 1
        return 0
    if spec_index >= len(specs):
        if all([c == "." or c == "?" for c in springs_]):
            return 1
        return 0
    if current == "?":
        cur = deepcopy(current_group)
        s = spec_index
        if force_skip:
            springs_.insert(0, ".")
            return count_(tuple(springs_), tuple(specs), tuple(cur), s)
        springs_.insert(0, "#")
        count_1 = count_(tuple(springs_), tuple(specs), tuple(cur), s)
        springs_.pop(0)
        cur = deepcopy(current_group)
        springs_.insert(0, ".")
        count_2 = count_(tuple(springs_), tuple(specs), tuple(cur), s)
        return count_1 + count_2
    if current == "#":
        current_group.append(current)
        if len(current_group) == specs[spec_index]:
            if not springs_:
                if spec_index >= len(specs) - 1:
                    return 1
                return 0
            if springs_[0] == "#":
                return 0
            spec_index += 1
            current_group = []
            return count_(
                tuple(springs_),
                tuple(specs),
                tuple(current_group),
                spec_index,
                force_skip=True,
            )
        return count_(tuple(springs_), tuple(specs), tuple(current_group), spec_index)
    if current == ".":
        if not current_group:
            return count_(
                tuple(springs_), tuple(specs), tuple(current_group), spec_index
            )
        if len(current_group) == specs[spec_index]:
            spec_index += 1
            current_group = []
            return count_(
                tuple(springs_),
                tuple(specs),
                tuple(current_group),
                spec_index,
                force_skip=True,
            )
        return 0
    return count_(tuple(springs_), tuple(specs), tuple(current_group), spec_index)



def main():
    input = get_input()
    sum = 0
    counts = []
    for row in input:
        springs, groups = get_springs(row, five_times=True)
        count = count_(tuple(springs), tuple(groups), tuple([]))
        counts.append(count)
        sum += count
    print(sum)

main()


# def test():
#     a = [".", "?", "?", ".", ".", "?", "?", ".", ".", ".", "?", "#", "#"]
#     b = ["?", "#", "#", "#", "?", "?", "?", "?", "?", "?", "?", "?"]
#     a_c = [1, 1, 3]
#     b_c = [3, 2, 1]
#     print(count_(tuple(a), tuple(a_c), tuple([])))
#     print(count_(tuple(b), tuple(b_c), tuple([])))
#     # print(get_springs(["*", "1,1,3"]))

# # test()
