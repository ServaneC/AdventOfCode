lines = open("input.txt", "r").readlines()

to_decode = lines[0].strip().split(",")

def decode(s):
    v = 0
    for c in s:
        v = (v + ord(c)) * 17 % 256
    return v 

r = 0
for s in to_decode:
    r += decode(s)

print(r)
