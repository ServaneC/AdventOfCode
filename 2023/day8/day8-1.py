lines = open("input.txt", "r").readlines()

direction = lines[0] 
network = {}

for l in lines[2:]:
    a, b = l.split("=")
    network[a.strip()] = b.strip("()\n ").replace(" ","").split(",")

current_node = 'AAA'
step = 0

while current_node != 'ZZZ':
    d = 0 if direction[step % (len(direction)-1)] == 'L' else 1
    current_node = network[current_node][d]
    step += 1
    
print(step)
