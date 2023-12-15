

def get_input():
    with open("15.txt", "r") as f:
        return [i for i in f.read().split(",")]
    

def algo(string):
    val = 0
    for s in string:
        val += ord(s)
        val = val *17
        val = val % 256
    return val

def box_contains_label(box, label):
    for i, item in enumerate(box):
        if label in item:
            print("true")
            return i
    return False

def interpret(ins, boxes):
    if "-" in ins:
        label, _ = ins.split("-")
        box = algo(label)
        i = box_contains_label(boxes[box], label)
        if type(i) == int:
            boxes[box].pop(i)

    if "=" in ins:
        label, lens = ins.split("=")
        box = algo(label)
        i = box_contains_label(boxes[box], label)
        if type(i) == int:
            boxes[box][i] = f"{label} {lens}"
        else:
            boxes[box].append(f"{label} {lens}")
    return boxes


def get_focus_power(item, box_num, box):
    slot = box.index(item) + 1
    _label, lens = item.split(" ")
    lens = int(lens)
    box_num +=1
    sum_ = box_num * slot * lens
    
    return sum_

def main():
    input = get_input()

    boxes = [[] for i in (range(256))]
    for i in input:
        boxes = interpret(i, boxes)
    sum = 0
    for i,box in enumerate(boxes):
        for item in box:
            power = get_focus_power(item, i, box)
            sum += power
    print(sum)



main()

# 212449