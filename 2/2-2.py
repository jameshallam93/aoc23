def get_input():
    with open("two.txt", "r") as f:
        return [
            l.replace("Game", "").replace("\n", "").split(":") for l in f.readlines()
        ]


def get_game_dict(games):
    game_dict = {}
    for g in games:
        game_dict[g[0]] = g[1].split(";")
    return game_dict


def get_game_totals(games):
    game_dict = {}
    for num, sets in games.items():
        game_dict[num] = {}
        for set in sets:
            cubes = set.split(",")
            for cube in cubes:
                quant, color = cube.strip().split(" ")
                if int(quant) > game_dict[num].get(color, 0):
                    game_dict[num][color] = int(quant)
    return game_dict


def get_total_score(game_dict):
    score = 0
    for _, quants in game_dict.items():
        prod = 1
        for quant in quants.values():
            prod *= quant
        score += prod
    return score


def main():
    input = get_input()
    game_dict = get_game_dict(input)
    game_dict = get_game_totals(game_dict)
    print(get_total_score(game_dict))


main()
