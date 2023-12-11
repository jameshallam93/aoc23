ENUM = {"L": 0, "R": 1}


def get_input():
    with open("8.txt", "r") as f:
        return [f.strip() for f in f.readlines()]


def create_dict(input):
    d = {}
    for i in input:
        print("i", i)
        if "LRR" in i:
            d["ins"] = i
            continue
        if not i:
            continue
        print(i.split("="))
        k, vs = i.split("=")
        k = k.replace(" ", "")
        v1, v2 = vs.replace("(", "").replace(")", "").replace(" ", "").split(",")
        d[k] = [v1, v2]
    return d


def follow(d, start, depth=0):
    next_ = start
    for i, letter in enumerate(d["ins"]):
        next_ = d[next_][ENUM[letter]]
        if next_ == "ZZZ":
            return depth * len(d["ins"]) + i + 1
    return follow(d, next_, depth + 1)


def main():
    input = get_input()
    d = create_dict(input)
    print(follow(d, "AAA"))


main()
