def get_input():
    with open("5.txt", "r") as f:
        return f.readlines()


def format_input(input):
    return_dict = {}
    current_title = ""
    current_map = []
    for i, l in enumerate(input):
        if i == 0:
            parts = l.split(": ")
            return_dict[parts[0]] = parts[1].split(" ")
            continue
        if input[i][0].isalpha():
            parts = l.split(" ")
            current_title = parts[0]
        if input[i][0].isdigit():
            parts = l.split(" ")
            current_map.append([p.replace("\n", "") for p in parts])
        if input[i][0] == "\n":
            return_dict[current_title] = current_map
            current_map = []
            current_title = ""
    return_dict[current_title] = current_map
    return return_dict


def get_current_map(input, current_map_prefix):
    current_map = [key for key in input.keys() if current_map_prefix in key]
    assert len(current_map) == 1
    current_map = current_map[0]
    return current_map


def follow_seed_to_location(val, map, current_map_prefix):
    # if we are past the x-to-location map, return the current value
    if current_map_prefix == "location-":
        return val
    current_map = get_current_map(map, current_map_prefix)
    next_map_prefix = current_map.split("-")[-1] + "-"
    for row in map[current_map]:
        dest, source, range_ = [int(i) for i in row]
        if source <= val and val <= source + range_:
            diff = val - source
            destination = dest + diff
            return follow_seed_to_location(
                destination, map, current_map_prefix=next_map_prefix
            )
    return follow_seed_to_location(val, map, current_map_prefix=next_map_prefix)


def follow_seeds(input):
    locs = []
    for seed in input["seeds"]:
        loc = follow_seed_to_location(int(seed), input, current_map_prefix="seed-")
        locs.append(loc)
    return locs


def main():
    input = get_input()
    input = format_input(input)
    locations = follow_seeds(input)
    print(min(locations))


main()
