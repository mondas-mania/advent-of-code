#  Should've gone BFS instead of DFS duh
import sys
visited = {}

def print_map(map: list):
  return "\n".join(["".join(line) for line in map])

def print_path(path: list, map: list):
  size = get_map_size(map)
  grid = [["." for _ in range(size[0])] for _ in range(size[1])]

  for i in range(len(path)):
    step = path[i]
    if i + 1 == len(path):
      grid[step[1]][step[0]] = "E"
    else:
      next_step = path[i+1]
      if next_step[0] > step[0]:
        grid[step[1]][step[0]] = ">"
      elif next_step[0] < step[0]:
        grid[step[1]][step[0]] = "<"

      if next_step[1] > step[1]:
        grid[step[1]][step[0]] = "v"
      elif next_step[1] < step[1]:
        grid[step[1]][step[0]] = "^"
  
  return print_map(grid)

def get_map_size(map: list):
  return (len(map[0]), len(map))

def get_start(map: list):
  for k in range(len(map)):
    for i in range(len(map[k])):
      if map[k][i] == "S":
        return (i, k)
  return (0,0)


def explore(map:list, pos: tuple, history: list):
  global visited
  history_list = []
  height = map[pos[1]][pos[0]] if map[pos[1]][pos[0]] != "S" else "a"
  map_size = get_map_size(map)
  new_history = history.copy()
  new_history.append(pos)

  if pos in visited.keys():
    if len(new_history) < visited[pos]:
      visited[pos] = len(new_history)
    else:
      return history_list
  else:
    visited[pos] = len(new_history)

  if height == "E":
    print(f"FOUND E AT {new_history}")
    history_list.append(new_history)
    return history_list

  north_pos = (pos[0], pos[1] - 1) if pos[1] - 1 >= 0 and (pos[0], pos[1] - 1) not in visited else None
  east_pos = (pos[0] + 1, pos[1]) if pos[0] + 1 < map_size[0] and (pos[0] + 1, pos[1]) not in visited else None
  south_pos = (pos[0], pos[1] + 1) if pos[1] + 1 < map_size[1] and (pos[0], pos[1] + 1) not in visited else None
  west_pos = (pos[0] - 1, pos[1]) if pos[0] - 1 >= 0 and (pos[0] - 1, pos[1]) not in visited else None

  north_height = (map[north_pos[1]][north_pos[0]] if map[north_pos[1]][north_pos[0]] != "E" else "z") if north_pos else None
  east_height = (map[east_pos[1]][east_pos[0]] if map[east_pos[1]][east_pos[0]] != "E" else "z") if east_pos else None
  south_height = (map[south_pos[1]][south_pos[0]] if map[south_pos[1]][south_pos[0]] != "E" else "z") if south_pos else None
  west_height = (map[west_pos[1]][west_pos[0]] if map[west_pos[1]][west_pos[0]] != "E" else "z") if west_pos else None

  if north_pos and ord(north_height) - ord(height) <= 1:
    history_list += explore(map, north_pos, new_history)
  if east_pos and ord(east_height) - ord(height) <= 1:
    history_list += explore(map, east_pos, new_history)
  if south_pos and ord(south_height) - ord(height) <= 1:
    history_list += explore(map, south_pos, new_history)
  if west_pos and ord(west_height) - ord(height) <= 1:
    history_list += explore(map, west_pos, new_history)

  return history_list

  
  

input_file = open('input.txt', 'r')
map = [list(line) for line in input_file.read().rstrip().split('\n')]
# print(print_map(map))

start_pos = get_start(map)

history_list = explore(map, start_pos, [])
print([len(history[1:]) for history in history_list])

path = history_list[0]

print(print_path(path, map))