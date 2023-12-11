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
                score = score + 1
    return score


def get_scores(cards):
    card_dict = {}
    for card in cards:
        card_num = str(card[0][5:8]).strip().replace(":", "")
        score = get_score_for_card(card)
        card_dict[int(card_num)] = {"score": score, "copies": 1}
    return card_dict


def increment_copies_for_card(card_dict, card_num):
    score = card_dict[card_num]["score"]
    for i in range(1, score + 1):
        if card_num + i > len(card_dict.keys()):
            return
        card_dict[card_num + i]["copies"] += card_dict[card_num]["copies"]


def sum_copies(card_dict):
    return sum([card_dict[i]["copies"] for i in card_dict.keys()])


def increment_copies(score_copies_dict):
    for card_num in score_copies_dict.keys():
        increment_copies_for_card(score_copies_dict, card_num)
    return score_copies_dict


def main():
    scratchcards = get_input()
    score_copies_dict = get_scores(scratchcards)
    score_copies_dict = increment_copies(score_copies_dict)
    total_scratchcards = sum_copies(score_copies_dict)
    print(total_scratchcards)


main()

# 9997537
