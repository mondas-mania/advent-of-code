file_name = "input.txt"
starting_pos = (0,0)
starting_dir = "R"

dir_conversions = {
  ".": {
    "L": ["L"],
    "U": ["U"],
    "D": ["D"],
    "R": ["R"],
  },
  "/": {
    "L": ["D"],
    "U": ["R"],
    "D": ["L"],
    "R": ["U"],
  },
  "\\": {
    "L": ["U"],
    "U": ["L"],
    "D": ["R"],
    "R": ["D"],
  },
  "-": {
    "L": ["L"],
    "R": ["R"],
    "U": ["L", "R"],
    "D": ["L", "R"],
  },
  "|": {
    "L": ["U", "D"],
    "R": ["U", "D"],
    "U": ["U"],
    "D": ["D"],
  }
}


def is_possible_neighbour(pos: tuple, doohickey: list) -> bool:
  max_cols = len(doohickey[0])
  max_rows = len(doohickey)
  return (pos[0] < max_rows and pos[0] >= 0) and (pos[1] < max_cols and pos[1] >= 0)

def next_cell_in_dir(pos: tuple, direction: str, doohickey: list) -> tuple:
  match direction:
    case "L":
      return (pos[0], pos[1] - 1)
    case "R":
      return (pos[0], pos[1] + 1)
    case "U":
      return (pos[0] - 1, pos[1])
    case "D":
      return (pos[0] + 1, pos[1])
    case _:
      print(f"Unknown direction: {direction}")
      return


def get_next_cells(current_pos: tuple, current_dir: str, doohickey: list) -> list:
  current_contents = doohickey[current_pos[0]][current_pos[1]]
  converted_dirs = dir_conversions[current_contents][current_dir]
  next_cells = []
  for new_dir in converted_dirs:
    next_cell = next_cell_in_dir(current_pos, new_dir, doohickey)
    if is_possible_neighbour(next_cell, doohickey):
      next_cells.append((next_cell, new_dir))

  return next_cells


def get_activated_count(paths: list):
  cells_visited = set()
  [[cells_visited.add(pos[0]) for pos in path] for path in paths]
  return len(cells_visited)


def traverse_doohickey(starting_pos: tuple, starting_dir: str, doohickey: list) -> list:
  finished_paths = []
  paths = [[(starting_pos, starting_dir)]]
  visited = [(starting_pos, starting_dir)]
  
  while len(paths) > 0:
    new_paths = []
    for path in paths:
      next_cells = get_next_cells(path[-1][0], path[-1][1], doohickey)
      if len(next_cells) == 0:
        finished_paths.append(path)
      for cell in next_cells:
        if cell in visited:
          finished_paths.append(path)
        else:
          visited.append(cell)
          new_path = path.copy()
          new_path.append(cell)
          new_paths.append(new_path)

    paths = new_paths.copy()

  return finished_paths
  

input_file = open(file_name, 'r')
doohickey = [list(line) for line in input_file.read().rstrip().split('\n')]

paths = traverse_doohickey(starting_pos, starting_dir, doohickey)
activated = get_activated_count(paths)

print(f"The number of activated cells is {activated}")
