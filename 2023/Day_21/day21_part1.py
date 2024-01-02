file_name = "input.txt"
no_steps = 64

def plot_garden(garden: list, targets: list) -> str:
  result = "\n".join(["".join(["O" if (i,j) in targets else spot for j, spot in enumerate(row)]) for i, row in enumerate(garden)])
  return result


def is_valid_pos(garden: list, current_pos: tuple) -> bool:
  max_rows = len(garden)
  max_cols = len(garden[0])
  row = current_pos[0]
  col = current_pos[1]
  return (row >= 0 and col >= 0) and (row < max_rows and col < max_cols) and garden[row][col] != "#"


def get_neighbouring_plots(garden: list, current_pos: tuple) -> set:
  row = current_pos[0]
  col = current_pos[1]
  possible_neighbours = [
    (row + 1, col),
    (row - 1, col),
    (row, col + 1),
    (row, col - 1)
  ]
  return set([neighbour for neighbour in possible_neighbours if is_valid_pos(garden, neighbour)])


def get_destinations(garden: list, start_pos: tuple, no_steps: int) -> list:
  current_locations = set([start_pos])
  for _ in range(no_steps):
    new_locs = set()
    for loc in current_locations:
      neighbours = get_neighbouring_plots(garden, loc)
      new_locs = new_locs | neighbours
    current_locations = new_locs
  return current_locations


input_file = open(file_name, 'r')
garden = [list(line) for line in input_file.read().rstrip().split('\n')]
start_pos = [(i, row.index("S")) for i, row in enumerate(garden) if "S" in row][0]

targets = get_destinations(garden, start_pos, no_steps)
total_dests = len(targets)
garden_str = plot_garden(garden, targets)
# print(garden_str)
print(f"There are {total_dests} possible destinations.")
