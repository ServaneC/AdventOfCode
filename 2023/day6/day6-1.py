lines = open("input.txt", "r").readlines()

times = [eval(x) for x in  lines[0].split(":")[1].split()]
dist = [eval(x) for x in  lines[1].split(":")[1].split()]

result = 1
for i in range(len(times)):
    m = 0
    for j in range(1, times[i]+1):
        if j * (times[i] - j) > dist[i]:
            m += 1
    result *= m

print(result)
