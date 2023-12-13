lines = open("input.txt", "r").readlines()

patterns = []

p = []
for line in lines:
    l = list(line.strip())
    if l != []:
        p.append(l)
    else:
        patterns.append(p)
        p = []
patterns.append(p)


def check_row(pattern, i):
    j = i - 1
    while i < len(pattern) and j >= 0:
        for idx in range(len(pattern[i])):
            if pattern[i][idx] != pattern[j][idx]:
                    return False
        j -= 1
        i += 1
    return True

# check rows for mirror
def check_rows(pattern):
    for i in range(1, len(pattern)):
        if check_row(pattern, i):
            return i
    return 0

def check_column(pattern, i):
    j = i - 1
    while i < len(pattern[0]) and j >= 0:
        for idx in range(len(pattern)):
            if pattern[idx][i] != pattern[idx][j]:
                return False
        j -= 1
        i += 1
    return True
    
def check_colums(pattern):
    for j in range(1, len(pattern[0])):
        if check_column(pattern, j):
            return j
    return 0

row_result = 0
column_result = 0
for pattern in patterns:
    r = check_rows(pattern)
    if r > 0:
        row_result += r
    else:
        column_result += check_colums(pattern)
        
print(row_result * 100 + column_result)
