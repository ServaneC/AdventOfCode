lines = open("input.txt", "r").readlines()

histories = [l.strip().split(" ") for l in lines]

def process_line(l):
    next = []
    for i in range (1, len(l)):
        next.append(l[i]-l[i-1])
    return next

def is_last_line(l):
    for i in l:
        if i != 0:
            return False
    return True

def compute_sequences_result(sequences):
    current = sequences[-1]
    current.append(0)
    for i in range(-2, -len(sequences)-1, -1):
        ta = current[-1]
        current = sequences[i]
        sequences[i].append(current[-1]+ta)
    return sequences[0][-1]
    
result = 0

for h in histories:
    current =  [eval(x) for x in  h]
    seqences = [current]
    while not is_last_line(current):
        current = process_line(current)
        seqences.append(current)
    result += compute_sequences_result(seqences)

print(result)
