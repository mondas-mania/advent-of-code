file_name = "input.txt"


def get_highest_values(bricks: list) -> tuple:
  highest_x = max([max(brick[0][0], brick[1][0]) for brick in bricks])
  highest_y = max([max(brick[0][1], brick[1][1]) for brick in bricks])
  highest_z = max([max(brick[0][2], brick[1][2]) for brick in bricks])
  return (highest_x, highest_y, highest_z)


def get_brick_cells(brick: list) -> list:
  positions = []
  x = [brick[0][0], brick[1][0]]
  y = [brick[0][1], brick[1][1]]
  z = [brick[0][2], brick[1][2]]
  for i in range(min(x), max(x) + 1):
    for j in range(min(y), max(y) + 1):
      for k in range(min(z), max(z) + 1):
        positions.append((i,j,k))
  return positions


def get_all_brick_cells(bricks: list) -> list:
  positions = []
  for brick in bricks:
    positions.append(get_brick_cells(brick))
  return positions


def sort_bricks(bricks: list, sort_axis: str = "z") -> list:
  axes = {'x': 0, 'y': 1, 'z': 2}
  ax = axes[sort_axis]
  new_bricks = sorted(bricks, key=lambda brick_pair: min(brick_pair[0][ax], brick_pair[1][ax]))
  return new_bricks


def plot_bricks(bricks: list, axis_hor: str, axis_ver: str = "z") -> str:
  max_values = get_highest_values(bricks)
  all_brick_cells = get_all_brick_cells(bricks)
  axes = {'x': 0, 'y': 1, 'z': 2}
  ax_hor = axes[axis_hor]
  ax_ver = axes[axis_ver]
  grid = [["-" if i == 0 and axis_ver == "z" else "." for _ in range(max_values[ax_hor] + 1)] for i in range(max_values[ax_ver] + 1)]

  for i, brick in enumerate(all_brick_cells):
    for pos in brick:
      pos_hor = pos[ax_hor]
      pos_ver = pos[ax_ver]
      grid[pos_ver][pos_hor] = chr(i + 65)

  return "\n".join(["".join(row) for row in grid[::-1]])


input_file = open(file_name, 'r')
bricks = [[tuple([int(pos) for pos in coords.split(",")]) for coords in line.split("~")] for line in input_file.read().rstrip().split('\n')]

sorted_bricks = sort_bricks(bricks)

string_bricks_x = plot_bricks(sorted_bricks[0:26], "x")
string_bricks_y = plot_bricks(sorted_bricks[0:26], "y")
string_bricks_x_y = plot_bricks(sorted_bricks[0:26], "x", "y")
print()
print(string_bricks_x)
print()
print(string_bricks_y)
print()
print(string_bricks_x_y)

None
