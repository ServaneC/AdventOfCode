lines = open("input.txt", "r").readlines()

mirrors = "/\\"
splitters = "|-"

beams = [[0, 0, '➡️']]

energized = [list(l.strip()) for l in lines]

def move(b):
    if b[2] == '⬆️':
        b[0] = b[0] - 1 if b[0] != 0 else b[0]
    elif b[2] == '⬇️':
        b[0] = b[0] + 1 if b[0] < len(lines) - 1 else b[0]
    elif b[2] == '⬅️':
        b[1] = b[1] - 1 if b[1] != 0 else b[1]
    elif b[2] == '➡️':
        b[1] = b[1] + 1 if b[1] < len(lines[0]) - 2 else b[1]

def handle_mirror(b, mirror):
    if b[2] == '⬆️':
        if mirror == '/':
            return '➡️'
        if mirror == '\\':
            return '⬅️'
    if b[2] == '⬇️':
        if mirror == '/':
            return'⬅️'
        if mirror == '\\':
            return '➡️'
    if b[2] == '⬅️':
        if mirror == '/':
            return '⬇️'
        if mirror == '\\':
            return '⬆️'
    if b[2] == '➡️':
        if mirror == '/':
            return '⬆️'
        if mirror == '\\':
            return '⬇️'

def handle_splitter(b, splitter):
    if splitter == '-' and b[2]  in "⬅️➡️" or \
        splitter == '|' and b[2] in "⬇️⬆️":
            return None
    if splitter == '-':
        return ['⬅️', '➡️']
    if splitter == '|':
        return ['⬇️', '⬆️']
        
changed = True
count = 0
while count < 3:
    to_append = []
    to_remove = []
    changed = False
    for b in beams:
        if energized[b[0]][b[1]] != '#':
            energized[b[0]][b[1]] = '#'
            changed = True
        before = b.copy()
        move(b)
        if before == b:
            to_remove.append(b)
        pos = lines[b[0]][b[1]]
        if pos == '.':
            continue
        if pos in mirrors:
            b[2] = handle_mirror(b, pos)
        if pos in splitters:
            new_dir = handle_splitter(b, pos)
            if new_dir is not None:
                b[2] = new_dir[0]
                nb = b.copy()
                nb[2] = new_dir[1]
                to_append.append(nb)
    if changed and count > 0:
        count = 0
    if not changed:
        count += 1
    for b in to_append:
        beams.append(b)
    for b in to_remove:
        beams.remove(b)

r = 0
for l in energized:
    r += l.count('#') 
    
print(r)
