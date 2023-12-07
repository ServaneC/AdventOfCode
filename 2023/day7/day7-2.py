lines = open("input.txt", "r").readlines()

hands = [l.strip().split(" ") for l in lines]

strenght = "J23456789TQKA"
joker = 'J'

fiveok = []
fourok = []
fh = []
tok = []
tp = []
op = []
hc = []

def is_five_of_kind(hand):
    for c in hand:
        if c != joker and hand.count(c) + hand.count(joker) == 5:
            return True
    return hand.count(joker) == 5

def is_four_of_kind(hand):
    for c in hand:
        if c != joker and hand.count(c) + hand.count(joker) == 4:
            return True
    return False
    
def is_full_house(hand):
    if is_three_of_kind(hand):
        jokers = hand.count(joker)
        three = ''
        for c in hand:
            if c != joker and hand.count(c) + hand.count(joker) == 3:
                jokers -= 3 - hand.count(c)
                three = c
                break
        for c in hand:
            if c != joker and c != three and hand.count(c) + jokers == 2:
                return True
    return False

def is_three_of_kind(hand):
    for c in hand:
        if c != joker and hand.count(c) + hand.count(joker) == 3:
            return True
    return False

def get_pairs(hand):
    p = []
    jokers = hand.count(joker)
    for c in hand:
        if c != joker and hand.count(c) + jokers == 2 and c not in p:
            jokers -= 2 - hand.count(c)
            p.append(c)
    return p

def is_two_pairs(hand):
   return len(get_pairs(hand)) == 2

def is_one_pair(hand):
    return len(get_pairs(hand)) == 1

def stronger_hand(h1, h2):
    for i in range(5):
        if h1[i] == h2[i]:
            continue
        elif strenght.index(h1[i]) > strenght.index(h2[i]):
            return h1
        else:
            return h2
    return h1

def bubblesort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if stronger_hand(arr[j][0], arr[j+1][0]) == arr[j][0]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return

def sort_hands(hands_tab):
    if len(hands_tab) <= 1:
        return hands_tab
    bubblesort(hands_tab)
    

for h in hands:
    hand = h[0]
    if is_five_of_kind(hand):
        fiveok.append(h)
    elif is_four_of_kind(hand):
        fourok.append(h)
    elif is_full_house(hand):
        fh.append(h)
    elif is_three_of_kind(hand):
        tok.append(h)
    elif is_two_pairs(hand):
        tp.append(h)
    elif is_one_pair(hand):
        op.append(h)
    else:
        hc.append(h)

i = 1
result = 0
for tab in [hc, op, tp, tok, fh, fourok, fiveok]:
    bubblesort(tab)
    for hand in tab:
        result += i * int(hand[1])
        i += 1

print(result)
