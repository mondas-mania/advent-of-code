file_name = "input.txt"
start_node = "AAA"
end_node = "ZZZ"

# way too much recursion oops
# def reach_destination(current_node: str, destination: str, directions: list, direction_index: int, nodes: dict) -> list:
#   if current_node == destination:
#     return [current_node]
  
#   direction = directions[direction_index]
#   next_step = nodes[current_node][0 if direction == "L" else 1]
#   path = [current_node]
#   direction_index = 0 if direction_index + 1 >= len(directions) else direction_index + 1
#   print(f"Going {direction} from {current_node} to {next_step}")
#   path += reach_destination(next_step, destination, directions, direction_index, nodes)
#   return path

input_file = open(file_name, 'r')
lines = [line for line in input_file.read().rstrip().split('\n')]
directions = list(lines[0])
nodes = {line.split(" = ")[0]: tuple(line.split(" = ")[1][1:-1].split(", ")) for line in lines[2:]}


current_node = start_node
direction_index = 0
path = []
while current_node != end_node:
  direction = directions[direction_index]
  next_step = nodes[current_node][0 if direction == "L" else 1]
  path.append(next_step)
  direction_index = 0 if direction_index + 1 >= len(directions) else direction_index + 1
  # print(f"Going {direction} from {current_node} to {next_step}")
  current_node = next_step
  pass


print(f"It takes {len(path)} steps to reach {end_node} from {start_node}.")
