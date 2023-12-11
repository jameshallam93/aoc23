import functools

CARD_STRENGTHS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def get_input():
    with open("7.txt", "r") as f:
        return [
            {f.strip().split(" ")[0]: f.strip().split(" ")[1]} for f in f.readlines()
        ]


def get_multiples(hand):
    multiples = {}
    for card in hand:
        count_ = hand.count(card)
        if count_ >= 1:
            if multiples.get(count_) is None:
                multiples[count_] = {card}
            else:
                multiples[count_].add(card)
    return multiples


def compare_card_strengths(hand_1, hand_2):
    hand_1 = list(list(hand_1.keys())[0])
    hand_2 = list(list(hand_2.keys())[0])
    while True:
        if CARD_STRENGTHS.index(hand_1[0]) > CARD_STRENGTHS.index(hand_2[0]):
            return 1
        elif CARD_STRENGTHS.index(hand_1[0]) < CARD_STRENGTHS.index(hand_2[0]):
            return -1
        else:
            hand_1.pop(0)
            hand_2.pop(0)


def get_hand_strength(hand):
    cards = list(hand.keys())[0]
    multiples = get_multiples(cards)
    if multiples.get(5) is not None:
        # five of a kind - 7
        return 7
    if multiples.get(4) is not None:
        # four of a kind - 6
        return 6
    if multiples.get(3) is not None:
        if multiples.get(2) is not None:
            # full house - 5
            return 5
        else:
            # three of a kind - 4
            return 4
    if multiples.get(2) is not None:
        if len(multiples.get(2)) == 2:
            # two pair - 3
            return 3
        else:
            # pair - 2
            return 2
    if multiples.get(1) is not None:
        # high card - 1
        return 1


def order(hand_1, hand_2):
    hand_str_1 = get_hand_strength(hand_1)
    hand_str_2 = get_hand_strength(hand_2)
    if hand_str_1 > hand_str_2:
        return 1
    elif hand_str_1 < hand_str_2:
        return -1
    else:
        return compare_card_strengths(hand_1, hand_2)


def order_hands(hands):
    return sorted(hands, key=functools.cmp_to_key(order))


def get_winnings(ordered):
    sum = 0
    for i, hand in enumerate(ordered):
        rank = i + 1
        bet = list(hand.values())[0]
        sum += rank * int(bet)
    return sum


def main():
    hands = get_input()
    ordered = order_hands(hands)
    winnings = get_winnings(ordered)
    print(winnings)


main()
