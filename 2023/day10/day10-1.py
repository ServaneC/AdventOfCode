lines = open("input.txt", "r").readlines()

# find start position

start = [0, 0]

max_x = len(lines)
max_y = len(lines[0])

for i, l in enumerate(lines):
    if 'S' in l:
        start = [i, l.find('S')]

ground = '.'
north = [-1, 0]
south = [+1, 0]
west = [0, -1]
east = [0, +1]

pipes = {
    '|': [south, north],
    '-': [west, east],
    'L': [north, east],
    'J': [west, north],
    '7': [west, south],
    'F': [south, east],
}

valid_north = "7|F"
valid_south = "J|L"
valid_west = "L-F"
valid_east = "J-7"

def next_pos(pos, toadd):
    x, y = pos[0]+toadd[0], pos[1]+toadd[1]
    x = x if x >= 0 and x < max_x else pos[0]
    y = y if y >= 0 and y < max_y else pos[1]
    if [x, y] == pos:
        return pos
    n = lines[x][y]
    if n is ground:
        return pos
    if toadd is north and n not in valid_north:
        return pos
    if toadd is south and n not in valid_south:
        return pos
    if toadd is east and n not in valid_east:
        return pos
    if toadd is west and n not in valid_west:
        return pos
    return [x, y]

def check_surrounding(pos):
    s = [next_pos(pos, north), next_pos(pos, east), next_pos(pos, south), next_pos(pos, west)]
    n = []
    for i, p in enumerate(s):
        if p is not pos:
            n.append(p)
    return n

def next_step(before, current):
    next_pos = []
    for p in pipes[lines[current[0]][current[1]]]:
        next_pos.append([current[0]+p[0], current[1]+p[1]])
    if next_pos[0] == before:
        return next_pos[1]
    return next_pos[0]            
        

paths = check_surrounding(start)
before = [start, start]

step = 1

while paths[0] != paths[1]:
    after = [next_step(before[0], paths[0]), next_step(before[1], paths[1])]
    before = paths
    paths = after
    step += 1

print(step)
