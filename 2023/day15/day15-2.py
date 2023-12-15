lines = open("input.txt", "r").readlines()

to_decode = lines[0].strip().split(",")

boxes = {}

def decode(s):
    v = 0
    for c in s:
        v = (v + ord(c)) * 17 % 256
    return v 

def add(box_idx, label, lens):
    if not box_idx in boxes:
        boxes[box_idx] = [[label, lens]]
        return
    for i, b in enumerate(boxes[box_idx]):
        if b[0] == label:
            boxes[box_idx][i][1] = lens
            return
    boxes[box_idx].append([label, lens])
    
def remove(box_idx, label):
    if not box_idx in boxes:
        return
    while True:
        d = False
        for i, b in enumerate(boxes[box_idx]):
            if b[0] == label:
                del boxes[box_idx][i]
                d = True
        if not d:
            return
        
for s in to_decode:
    label = s.split("=")[0].split("-")[0]
    print(label)
    if s[len(label)] == '=':
        add(decode(label), label, s[len(label)+1])
    else:
        remove(decode(label), label)

r = 0
for k in range(256):
    if k in boxes:
         for i, b in enumerate(boxes[k]):
            r += (k + 1) * (i + 1) * int(b[1])

print(r)

# 28158 too low
