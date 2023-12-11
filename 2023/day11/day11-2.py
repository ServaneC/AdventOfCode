lines = open("input.txt", "r").readlines()

lines = [list(l.strip()) for l in lines]

empty_lines = []
empty_column = []

# double full dot line and columns 
for i, l in enumerate(lines):
    if l.count('.') == len(l):
        empty_lines.append(i)

for i in range(len(lines[0])):
    empty = True
    for j in range(len(lines)):
        if lines[j][i] != '.':
            empty = False
            break
    if empty:
        empty_column.append(i)

glx = []

# find galaxies
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == '#':
            glx.append([i, j])

def compute_dist(a, b):
    dist = abs(b[0] - a[0]) + abs(b[1] - a[1])
    for i in range(min(a[0], b[0]), max(a[0], b[0])):
        if i in empty_lines:
            dist += 1000000 - 1
    for i in range(min(a[1], b[1]), max(a[1], b[1])):
        if i in empty_column:
            dist += 1000000 - 1
    return  dist

r = 0
for i, a in enumerate(glx):
    for b in glx[i+1:]:
        r += compute_dist(a, b)
print(r)
