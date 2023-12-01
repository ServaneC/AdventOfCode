file = open("input.txt", "r")

result = 0

for line in file:
    nbs = []
    for i, c in enumerate(line):
        if c.isdigit():
            nbs.append(c)
    result += int(nbs[0]) * 10 + int(nbs[-1])

print(result)
