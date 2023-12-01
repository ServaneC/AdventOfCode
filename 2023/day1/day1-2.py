file = open("input.txt", "r")

result = 0

num = {
    "one": "o1ne",
    "two": "t2wo",
    "three": "th3ree",
    "four": "fo4ur",
    "five": "fi5ve",
    "six": "si6x",
    "seven": "se7ven",
    "eight": "eig8ht",
    "nine": "ni9ne",
}

for line in file:
    nbs = []
    for word, nb in num.items():
        line = line.replace(word, str(nb))
    for i, c in enumerate(line):
        if c.isdigit():
            nbs.append(c)
    result += int(nbs[0]) * 10 + int(nbs[-1])

print(result)
