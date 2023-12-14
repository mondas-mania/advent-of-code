file_name = "input.txt"

def get_distance(pos_1: tuple, pos_2: tuple):
  x_dist = abs(pos_1[0] - pos_2[0])
  y_dist = abs(pos_1[1] - pos_2[1])
  return x_dist + y_dist

def copy_grid(grid: list) -> list:
  new_grid = []
  for row in grid:
    new_grid.append(row.copy())
  return new_grid

def transpose(grid: list) -> list:
  new_grid = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]
  return new_grid

def add_rows(grid: list) -> list:
  new_grid = []
  for row in grid:
    new_grid.append(row.copy())
    if "#" not in row:
      new_grid.append(row.copy())
  return new_grid

def expand_grid(grid: list) -> list:
  new_grid = add_rows(grid)
  transposed_grid = transpose(new_grid)
  new_grid = add_rows(transposed_grid)
  return transpose(new_grid)

def get_galaxy_distances(galaxies: list) -> dict:
  distance_dict = {i: {} for i in range(len(galaxies))}
  for i, galaxy_pos_a in enumerate(galaxies):
    for j, galaxy_pos_b in enumerate(galaxies):
      if j not in distance_dict[i].keys():
        distance = get_distance(galaxy_pos_a, galaxy_pos_b)
        distance_dict[i][j] = distance
        distance_dict[j][i] = distance
  return distance_dict


input_file = open(file_name, 'r')
grid = [list(line) for line in input_file.read().rstrip().split('\n')]

expanded_grid = expand_grid(grid)
galaxy_positions = []
[[galaxy_positions.append((i, j)) for j in range(len(expanded_grid[i])) if expanded_grid[i][j] == "#"] for i in range(len(expanded_grid))]

distance_dict = get_galaxy_distances(galaxy_positions)
pairs_sum = int(sum([sum(pair_dict.values()) for pair_dict in distance_dict.values()])/2)
print(f"The sum of all distances between galaxies is {pairs_sum}")
