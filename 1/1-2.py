import re

NUMS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_alpha_regex():
    return re.compile("[a-zA-Z]")


def get_input():
    with open("1.txt", "r") as f:
        return f.read().splitlines()


def sub_nums(input_list):
    inp = []
    regex = get_alpha_regex()
    for i in input_list:
        i = replace_first_and_last(i)
        i = regex.sub("", i)
        inp.append(i)
    return inp


def get_first_or_last(positions, pos):
    func = max if pos == "last" else min
    pos = func(positions.keys())
    return pos, positions[pos]


def replace_(string, pos, num):
    string = list(string)
    string[pos] = str(num)
    string = "".join(string)
    return string


def replace_first_and_last(string):
    num_string_positions = {
        string.find(i): i for i in NUMS.keys() if string.find(i) != -1
    }
    r_num_string_positions = {
        string.rfind(i): i for i in NUMS.keys() if string.rfind(i) != -1
    }
    if not num_string_positions or not r_num_string_positions:
        return string

    first_pos, first_num = get_first_or_last(num_string_positions, "first")
    last_pos, last_num = get_first_or_last(r_num_string_positions, "last")
    string = replace_(string, first_pos, NUMS[first_num])
    string = replace_(string, last_pos, NUMS[last_num])

    return string


def get_first_and_last(string):
    return int(string[0] + string[-1])


def main():
    input = get_input()
    input_list = sub_nums(input)
    print(sum(get_first_and_last(i) for i in input_list))


main()

# 57345
