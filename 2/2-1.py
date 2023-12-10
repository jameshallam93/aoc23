CUBES = {"red": 12, "green": 13, "blue": 14}


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


def strip_impossible_games(game_dict):
    for num, sets in game_dict.items():
        for set in sets:
            cubes = set.split(",")
            for cube in cubes:
                quant, color = cube.strip().split(" ")
                if CUBES[color] < int(quant) and game_dict.get(num):
                    game_dict[num] = None
    return game_dict


def get_score(game_dict):
    score = 0
    for num, sets in game_dict.items():
        if sets:
            score += int(num)
    return score


def main():
    input = get_input()
    game_dict = get_game_dict(input)
    game_dict = strip_impossible_games(game_dict)
    score = get_score(game_dict)
    print(score)


main()
