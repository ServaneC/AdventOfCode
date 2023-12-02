file = open("input.txt", "r")

games = []
# [r, g, b]
for line in file:
    sizes = [0, 0, 0]
    for s in line.split(":")[1].split(";"):
        for c in s.split(","):
            n, color = c.strip().split()
            n = int(n)
            sizes[0] = n if color == "red" and n > sizes[0] else sizes[0]
            sizes[1] = n if color == "green" and n > sizes[1] else sizes[1]
            sizes[2] = n if color == "blue" and n > sizes[2] else sizes[2]
    games.append(sizes)

result = 0
for game in games:
    result += game[0] * game[1] * game[2]

print(result)
