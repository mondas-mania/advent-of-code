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
shortest_val = 100000
shortest_intersect = crossings[0]

for cross in crossings:
    if cross[0] != 0 or cross[1] != 0:
        steps_1 = p.index(cross)
        steps_2 = q.index(cross)
        if steps_1 + steps_2 < shortest_val:
            shortest_intersect = cross
            shortest_val = steps_1 + steps_2

print(shortest_intersect)
print("Total steps: " + str(shortest_val))
print("P steps: " + str(p.index(shortest_intersect)))
print("Q steps: " + str(q.index(shortest_intersect)))
