file_name = "input.txt"
expansion_rate = 1000000


def get_distance(pos_1: tuple, pos_2: tuple, expansions: dict) -> int:
  min_row, max_row = min(pos_1[0], pos_2[0]), max(pos_1[0], pos_2[0])
  min_col, max_col = min(pos_1[1], pos_2[1]), max(pos_1[1], pos_2[1])
  row_expansions = [i for i in range(min_row, max_row) if i in expansions["rows"]]
  col_expansions = [i for i in range(min_col, max_col) if i in expansions["cols"]]
  row_dist = abs(pos_1[0] - pos_2[0]) + ((expansion_rate - 1) * len(row_expansions))
  col_dist = abs(pos_1[1] - pos_2[1]) + ((expansion_rate - 1) * len(col_expansions))
  return row_dist + col_dist


def transpose(grid: list) -> list:
  new_grid = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]
  return new_grid


def get_expansions(grid: list) -> dict:
  expansions = {}
  expansions["cols"] = []
  expansions["rows"] = []

  for i in range(len(grid)):
    if "#" not in grid[i]:
      expansions["rows"].append(i)

  transposed_grid = transpose(grid)

  for i in range(len(transposed_grid)):
    if "#" not in transposed_grid[i]:
      expansions["cols"].append(i)

  return expansions


def get_galaxy_distances(galaxies: list, expansions: dict) -> dict:
  distance_dict = {i: {} for i in range(len(galaxies))}
  for i, galaxy_pos_a in enumerate(galaxies):
    for j, galaxy_pos_b in enumerate(galaxies):
      if j not in distance_dict[i].keys():
        distance = get_distance(galaxy_pos_a, galaxy_pos_b, expansions)
        distance_dict[i][j] = distance
        distance_dict[j][i] = distance
  return distance_dict


input_file = open(file_name, 'r')
grid = [list(line) for line in input_file.read().rstrip().split('\n')]

expansions = get_expansions(grid)
galaxy_positions = []
[[galaxy_positions.append((i, j)) for j in range(len(grid[i])) if grid[i][j] == "#"] for i in range(len(grid))]

distance_dict = get_galaxy_distances(galaxy_positions, expansions)
pairs_sum = int(sum([sum(pair_dict.values()) for pair_dict in distance_dict.values()])/2)
print(f"The sum of all distances between galaxies is {pairs_sum}")
