lines = open("input.txt", "r").readlines()

seeds = lines[0].split(":")[1].split()

def is_in_range(nb, info):
    return nb in range(info[1], info[1]+info[2])

def get_dest_value(nb, info):
    return info[0] + (info[2] - (info[1] + info[2] - nb))

def from_elem1_to_elem2(array1, array2, to_map):
    for i, a in enumerate(array1):
        for info in to_map:
            if is_in_range(a, info):
                array2[i] = get_dest_value(a, info)

def read_map(i):
    ret = []
    for j, l in enumerate(lines[i+1:]):
        tab = l.split()
        if len(tab) != 3:
            return ret
        tab = [eval(x) for x in tab]
        ret.append(tab)
    return ret

array2 = [eval(x) for x in seeds]

for i, l in enumerate(lines):
    if "-to-" in l:
        array1 = array2.copy()
        from_elem1_to_elem2(array1, array2, read_map(i))

print(min(array2))
