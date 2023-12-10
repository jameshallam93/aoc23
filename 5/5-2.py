import time


def get_input():
    with open("fivetest.txt", "r") as f:
        return f.readlines()


def format_input(input):
    return_dict = {}
    map_title = ""
    current_map = []
    # there is 100% an easier way to do this,
    # but this works.
    for i, l in enumerate(input):
        if i == 0:
            parts = l.split(": ")
            return_dict[parts[0]] = parts[1].split(" ")
            continue
        first_letter = input[i][0]
        if first_letter.isalpha():
            # this is the start of a new map section
            parts = l.split(" ")
            map_title = parts[0]
        if first_letter.isdigit():
            # this is a row in the current map section
            parts = l.split(" ")
            current_map.append([p.replace("\n", "") for p in parts])
        if first_letter == "\n":
            # this is the end of a map section
            return_dict[map_title] = current_map
            current_map = []
            map_title = ""
    # capture details of last map section, since there is no newline at the end
    return_dict[map_title] = current_map
    return return_dict


def get_seed_ranges(seeds):
    # takes a list of numbers and returns a list of pairs of numbers
    pairs = []
    pair = []
    for i, s in enumerate(seeds):
        pair.append(int(s))
        if i % 2 == 0:
            continue
        else:
            pairs.append(pair)
            pair = []
    return pairs


def get_current_map(input, current_map_suffix):
    # find the current map key from the given suffix
    current_map = [key for key in input.keys() if current_map_suffix in key]
    assert len(current_map) == 1
    current_map = current_map[0]
    return current_map


def get_seed_or_none(seed_ranges, val):
    for [frm, to] in seed_ranges:
        if val >= frm and val <= frm + to:
            print(f"found matching seed value: {val}")
            return val
    return None


def find_seed_from_loc(input, val, current_map_suffix):
    """
    Recursive function which works backwards from a location value to
    find any corresponding seed values.
    """
    # if we are at the start of the map chain (i.e. trying to do x-to-seed):
    if current_map_suffix == "-seed":
        seed_ranges = get_seed_ranges(input["seeds"])
        return get_seed_or_none(seed_ranges, val)

    current_map = get_current_map(input, current_map_suffix)
    # next map suffix will always have the prefix of the current map suffix
    # e.g. x-to-y will always point to the next map suffix of z-to-x
    next_map_suffix = "-" + current_map.split("-")[0]

    for row in input[current_map]:
        dest, src, range_ = [int(i) for i in row]
        # if the current value is in the range of the current row:
        if val >= dest and dest + range_ > val:
            new_val = val + src - dest
            # continue up the chain using the new value
            return find_seed_from_loc(input, new_val, next_map_suffix)
    # if the current value is not in any of the ranges of the current map:
    # continue up the chain using the same value as previously
    return find_seed_from_loc(input, val, next_map_suffix)


def find_lowest_location(input):
    #  brute force babyyyyy
    r = 10000000
    for loc in range(r):
        # uncomment for progress tracking - will slow down code by around 30%
        # if loc % (r/100) == 0:
        #     print(f"Currently {loc/r*100}% done")
        seed = find_seed_from_loc(input, loc, current_map_suffix="-location")
        if seed != None:
            return loc


def main():
    t = time.perf_counter()
    input = format_input(get_input())
    lowest_loc = find_lowest_location(input)
    print(f"for location value: {lowest_loc}")
    t_f = time.perf_counter()
    print(f"finished in {t_f - t} seconds")


main()

# 9622622
