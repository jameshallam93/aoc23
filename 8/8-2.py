import math

ENUM = {"L": 0, "R": 1}


def get_input():
    with open("8.txt", "r") as f:
        return [f.strip() for f in f.readlines()]


def create_dict(input):
    d = {}
    for i in input:
        if "LRR" in i:
            d["ins"] = i
            continue
        if not i:
            continue
        k, vs = i.split("=")
        k = k.replace(" ", "")
        v1, v2 = vs.replace("(", "").replace(")", "").replace(" ", "").split(",")
        d[k] = [v1, v2]
    return d


def get_starting_group(input):
    group = []
    for i in input:
        if i.endswith("A"):
            group.append(i)
    return group


def follow(d, start, depth=0):
    next_ = start
    for i, letter in enumerate(d["ins"]):
        next_ = d[next_][ENUM[letter]]
        if next_.endswith("Z"):
            return depth * len(d["ins"]) + i + 1
    return next_


def main():
    input = get_input()
    d = create_dict(input)
    nexts = get_starting_group(d)
    depth = 0
    lengths = []
    for n in nexts:
        depth = 0
        next_ = n
        while True:
            next_ = follow(d, next_, depth)
            if type(next_) == int:
                lengths.append(next_)
                break
            depth += 1
    print(math.lcm(*lengths))


main()

#  8429602563785865 too high
#  9064949303801
