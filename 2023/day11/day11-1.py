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

empty_lines.reverse()
empty_column.reverse()

for i in empty_lines:
    lines.insert(i, ['.' * len(lines[0])])

for i in empty_column:
    for j in range(len(lines)):
        lines[j].insert(i, '.')

glx = []

# find galaxies
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == '#':
            glx.append([i, j])
r = 0
for i, a in enumerate(glx):
    for b in glx[i+1:]:
        r += abs(b[0] - a[0]) + abs(b[1] - a[1])
print(r)
