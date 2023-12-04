file = open("input.txt", "r")

cards = []
result = 0

for line in file:
    winning, mine = line.split(":")[1].split("|")
    winning = winning.strip().split()
    mine = mine.strip().split(" ")
    card_result = 0
    for n in mine:
        if n == '':
            continue
        if n in winning:
            card_result = card_result * 2 if card_result > 0 else 1
    result += card_result

print(result)
