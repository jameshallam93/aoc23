import re


def get_alpha_regex():
    return re.compile("[a-zA-Z]")


def get_input():
    regex = get_alpha_regex()
    with open("one.txt", "r") as f:
        return [regex.sub("", l) for l in f.read().splitlines()]


def get_first_and_last(string):
    return int(string[0] + string[-1])


def main():
    input = get_input()
    print(sum(get_first_and_last(i) for i in input))


main()

# 57346
