lines = open("input.txt", "r").readlines()

direction = lines[0] 
network = {}

current_nodes = []

for l in lines[2:]:
    a, b = l.split("=")
    node = a.strip()
    network[node] = b.strip("()\n ").replace(" ","").split(",")
    if node[2] == 'A':
        current_nodes.append(node)

def get_steps(node):
    step = 0
    while node[2] != 'Z':
        d = 0 if direction[step % (len(direction)-1)] == 'L' else 1
        node = network[node][d]
        step += 1
    return step

steps = [get_steps(node) for node in current_nodes]

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

lcm = 1
for step in steps:
    lcm = lcm * step // gcd(lcm, step)

print(lcm)
