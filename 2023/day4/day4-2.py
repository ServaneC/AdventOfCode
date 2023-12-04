lines = open("input.txt", 'r').readlines()

cards = [1 for i in range(len(lines))]

for i, line in enumerate(lines):
    winning, mine = line.split(":")[1].split("|")
    winning = winning.strip().split()
    mine = mine.strip().split(" ")
    nb_match = 0
    for n in mine:
        if n == '':
            continue
        if n in winning:
            nb_match += 1
    if nb_match > 0:
        for idx in range(nb_match):
            cards[i+idx+1] += cards[i]

print(sum(cards))
