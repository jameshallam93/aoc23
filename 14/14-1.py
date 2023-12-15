
DIR = [-1, 0]


def get_input():
    with open("14.txt", "r") as f:
        lines = f.readlines()
        return [list(l.strip()) for l in lines if l != ""]
        return [l.strip().split("\n") for l in f.readlines() if l != ""]




def move_boulder(rocks, coords):
    c = coords
    r = rocks
    while True:
        if r[c[0]][c[1]] != "O":
            return r
        next_ = [c[0] + DIR[0], c[1] + DIR[1]]
        if next_[0] < 0 or next_[1] < 0:
            return r
        if r[next_[0]][next_[1]] == "#":
            return r
        elif r[next_[0]][next_[1]] == "O":
            return r
        elif r[next_[0]][next_[1]] == ".":
            print("moving to ", next_)
            print(c, next_)
            r[c[0]][c[1]] = "."
            r[next_[0]][next_[1]] = "O"
            c = next_
        

def count_rows(rocks):
    count = 0
    for i, l in enumerate(rocks):
        for  c in l:
            if c == "O":
                print("adding ", i)
                count += len(rocks)-i
    return count

def main():
    rocks = get_input()
    for l in rocks:
        print(l)
    print("\n")
    for i, l in enumerate(rocks):
        for j,r in enumerate(l):
            rocks = move_boulder(rocks, [i, j])
    for l in rocks:
        print(l)
    print(count_rows(rocks))

main()

# 108840