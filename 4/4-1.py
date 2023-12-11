def get_input():
    with open("4.txt", "r") as f:
        return [l.strip().split("\n") for l in f.readlines() if l != ""]


def get_score_for_card(scratchcard):
    winning, actual = scratchcard[0].split("|")
    winning = winning.split(":")[1].split(" ")
    actual = actual.split(" ")
    score = 0
    for w in winning:
        if w != "":
            if w in actual:
                if score == 0:
                    score = 1
                else:
                    score = score * 2
    return score


def get_total_score(scractchcards):
    score = 0
    for card in scractchcards:
        points = get_score_for_card(card)
        score += points
    return score


def main():
    scratchcard_dict = get_input()
    score = get_total_score(scratchcard_dict)
    print(score)


main()

#  26218
