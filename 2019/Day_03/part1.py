import pandas as pd

input1 = list(pd.read_csv('input.txt', header=None).iloc[0])
input2 = list(pd.read_csv('input.txt', header=None).iloc[1])

p = [(0, 0)]
q = [(0, 0)]

# Right is +ve x
# Up is +ve y

for instr in input1:
    direction = instr[0]
    length = int(instr[1:])
    multip = 1
    if direction == "L" or direction == "D":
        multip *= -1

    prev_x = p[-1][0]
    prev_y = p[-1][1]

    if direction == "L" or direction == "R":
        for i in range(1, length+1):
            p.append((prev_x + multip*i, prev_y))
    else:
        for i in range(1, length+1):
            p.append((prev_x, prev_y + multip*i))

for instr in input2:
    direction = instr[0]
    length = int(instr[1:])
    multip = 1
    if direction == "L" or direction == "D":
        multip *= -1

    prev_x = q[-1][0]
    prev_y = q[-1][1]

    if direction == "L" or direction == "R":
        for i in range(1, length+1):
            q.append((prev_x + multip*i, prev_y))
    else:
        for i in range(1, length+1):
            q.append((prev_x, prev_y + multip*i))

print(p[-1])
print(q[-1])

crossings = list(set(p) & set(q))
print(crossings)
shortest_manhattan = crossings[0]
for cross in crossings:
    if cross[0] != 0 or cross[1] != 0:
        if abs(cross[0]) + abs(cross[1]) < abs(shortest_manhattan[0]) + abs(shortest_manhattan[1]):
            shortest_manhattan = cross

print(shortest_manhattan)
print(abs(shortest_manhattan[0]) + abs(shortest_manhattan[1]))
