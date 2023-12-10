import functools

CARD_STRENGTHS = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def get_input():
    with open("seven.txt", "r") as f:
        return [
            {f.strip().split(" ")[0]: f.strip().split(" ")[1]} for f in f.readlines()
        ]


def get_multiples(hand):
    """
    Returns a dict of the form:
    {
        1: {card1, card2, ...},
        2: {card1, card2, ...},
        3: {card1, card2, ...},
        4: {card1, card2, ...},
        5: {card1, card2, ...},
        "J": jokers
    }
    where the key is the number of cards in the hand and the value is a set of the cards
    Jokers are represented by the key "J", with the value being the total number of jokers.
    (it just makes it easier to process)
    """
    multiples = {}
    jokers = hand.count("J")
    for card in hand:
        if card == "J":
            continue
        count_ = hand.count(card)
        if count_ >= 1:
            if multiples.get(count_) is None:
                multiples[count_] = {card}
            else:
                multiples[count_].add(card)
    multiples["J"] = jokers
    return multiples


def get_hand_strength(hand):
    # this is a disgusting function
    cards = list(hand.keys())[0]
    multiples = get_multiples(cards)
    jokers = multiples.get("J", 0)
    if jokers == 5:  # five of a kind - 7
        return 7
    if multiples.get(5) is not None: # five of a kind - 7
        return 7
    if multiples.get(4) is not None:
        if jokers == 1: # five of a kind - 7
            return 7
        return 6 # four of a kind - 6
    if multiples.get(3) is not None:
        if jokers == 2: # five of a kind - 7
            return 7
        if jokers == 1: # four of a kind - 6
            return 6
        if multiples.get(2) is not None: # full house - 5
            return 5
        return 4 # three of a kind - 4
    if multiples.get(2) is not None:
        if jokers == 3: # five of a kind - 7
            return 7
        if jokers == 2: # four of a kind - 6
            return 6
        if len(multiples.get(2)) == 2:
            if jokers == 1: # full house - 5
                return 5
            return 3 # two pair - 3
        if jokers == 1: # three of a kind - 4
            return 4
        return 2 # pair - 2
    if jokers == 4: # five of a kind - 7
        return 7
    if jokers == 3: # four of a kind - 6
        return 6
    if jokers == 2: # three of a kind - 4
        return 4
    if jokers == 1: #  pair - 2
        return 2
    return 1 # high card - 1


def compare_card_strength(hand_1, hand_2):
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
            if len(hand_1) == 0:
                return 0


def order(hand_1, hand_2):
    hand_str_1 = get_hand_strength(hand_1)
    hand_str_2 = get_hand_strength(hand_2)
    if hand_str_1 > hand_str_2:
        return 1
    elif hand_str_1 < hand_str_2:
        return -1
    else:
        return compare_card_strength(hand_1, hand_2)


def order_hands(hands):
    ordered = sorted(hands, key=functools.cmp_to_key(order))
    return ordered


def get_winnings(ordered):
    sum = 0
    for i, hand in enumerate(ordered):
        rank = i + 1
        bet = list(hand.values())[0]
        sum += rank * int(bet)
    return sum


def main():
    input = get_input()
    ordered = order_hands(input)
    winnings = get_winnings(ordered)
    print(winnings)


main()


#  255730474 too high
#  255725809 too high
#  254414073 too low
#  253496970 too low
#  253733312 too low
#  254326370 wrong
#  254329870 wrong
#  254837398 correct
