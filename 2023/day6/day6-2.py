lines = open("input.txt", "r").readlines()

times = int(lines[0].split(":")[1].replace(" ", ""))
dist = int(lines[1].split(":")[1].replace(" ", ""))

# why think of a faster solution when we can just wait a few seconds

result = 0
for j in range(1, times+1):
    if j * (times - j) > dist:
        result += 1

print(result)
