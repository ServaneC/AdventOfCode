lines = open("input.txt", "r").readlines()

times = lines[0].split(":")[1].split()
dist = lines[1].split(":")[1].split()


def possible_hold_times(t, d):
    ret = []
    for i in range(1, t+1):
        dist = i * (t - i)
        if dist > d:
            ret.append(i)
    return ret

result = 1
for i in range(len(times)):
    result *= len(possible_hold_times(times[i], dist[i]))

print(result)
