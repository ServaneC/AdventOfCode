lines = open("input.txt", "r").readlines()

times = int(lines[0].split(":")[1].replace(" ", ""))
dist = int(lines[1].split(":")[1].replace(" ", ""))

# why think of a faster solution when we can just wait a few seconds

def possible_hold_times(t, d):
    ret = []
    for i in range(1, t+1):
        dist = i * (t - i)
        if dist > d:
            ret.append(i)
    return ret

result = 1 * len(possible_hold_times(times, dist))

print(result)
