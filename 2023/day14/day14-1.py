lines = open("input.txt", "r").readlines()

lines = [list(x) for x in lines]

for i in range(len(lines)//2):
    for x in range(len(lines)-1, 0, -1):
        for y in range(len(lines[x])):
            if lines[x][y] == "O" and lines[x-1][y] == ".":
                lines[x][y], lines[x-1][y]  = lines[x-1][y], lines[x][y]
           

r = 0
pts = len(lines)
for l in lines:
    r += pts * l.count('O')
    pts -= 1

print(r)
