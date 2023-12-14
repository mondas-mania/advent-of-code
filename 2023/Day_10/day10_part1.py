file_name = "input.txt"

def is_valid_pos(pos: tuple, grid: list) -> bool:
  row = pos[0]
  col = pos[1]
  max_rows = len(grid)
  max_col = len(grid[row])
  return True if row >= 0 and col >= 0 and row <= max_rows and col <= max_col else False

def get_valid_neighbours(pos: tuple, grid: list) -> list:
  row = pos[0]
  col = pos[1]
  current_pipe = grid[row][col]
  valid_neighbours = []

  match current_pipe:
    case "S":
      possible_neighbours = [possible for possible in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)] if is_valid_pos(possible, grid)]
      for neighbour in possible_neighbours:
        # if current pos is a valid neighbour of a neighbouring cell then it's a valid destination
        if pos in get_valid_neighbours(neighbour, grid):
          valid_neighbours.append(neighbour)
    case "|":
      valid_neighbours = [possible for possible in [(row - 1, col), (row + 1, col)] if is_valid_pos(possible, grid)]
    case "-":
      valid_neighbours = [possible for possible in [(row, col - 1), (row, col + 1)] if is_valid_pos(possible, grid)]
    case "L":
      valid_neighbours = [possible for possible in [(row - 1, col), (row, col + 1)] if is_valid_pos(possible, grid)]
    case "J":
      valid_neighbours = [possible for possible in [(row - 1, col), (row, col - 1)] if is_valid_pos(possible, grid)]
    case "7":
      valid_neighbours = [possible for possible in [(row + 1, col), (row, col - 1)] if is_valid_pos(possible, grid)]
    case "F":
      valid_neighbours = [possible for possible in [(row + 1, col), (row, col + 1)] if is_valid_pos(possible, grid)]
    case ".":
      pass
    case _:
      print(f"Unknown pipe {current_pipe} at {pos}")
  
  return valid_neighbours

def find_farthest(starting_pos: tuple, grid: list) -> int:
  next_steps = get_valid_neighbours(starting_pos, grid)
  paths = [[starting_pos], [starting_pos]]
  while next_steps[0] != next_steps[1]:
    for i in range(2):
      neighbours = get_valid_neighbours(next_steps[i], grid)
      neighbours.remove(paths[i][-1])
      paths[i].append(next_steps[i])
      next_steps[i] = neighbours[0]
  
  # print(f"Reached {next_steps[0]} after {len(paths[0])} with paths {paths[0]} and {paths[1]}")
  print(f"Reached {next_steps[0]} after {len(paths[0])}")
  return len(paths[0])


input_file = open(file_name, 'r')
grid = [list(line) for line in input_file.read().rstrip().split('\n')]
starting_pos = [(i, grid[i].index("S")) for i in range(len(grid)) if "S" in grid[i]][0]

dist = find_farthest(starting_pos, grid)
None