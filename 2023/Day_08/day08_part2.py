file_name = "input.txt"
start_letter = "A"
end_letter = "Z"

input_file = open(file_name, 'r')
lines = [line for line in input_file.read().rstrip().split('\n')]
directions = list(lines[0])
nodes = {line.split(" = ")[0]: tuple(line.split(" = ")[1][1:-1].split(", ")) for line in lines[2:]}


current_nodes = [node for node in list(nodes.keys()) if node[-1] == start_letter]
direction_index = 0
path = []
print(f"Starting at {current_nodes}")
while not all([node[-1] == end_letter for node in current_nodes]):
  direction = directions[direction_index]
  direction_index = 0 if direction_index + 1 >= len(directions) else direction_index + 1
  for i, node in enumerate(current_nodes):
    current_nodes[i] = nodes[node][0 if direction == "L" else 1]
  print(f"Going {direction} to {current_nodes}")
  path.append(current_nodes)



print(f"It takes {len(path)} steps to reach {end_letter} from {start_letter}.")
