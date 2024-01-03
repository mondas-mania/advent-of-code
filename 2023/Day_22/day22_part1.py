file_name = "input_test.txt"


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
      grid[pos_ver][pos_hor] = chr(i + 65) if grid[pos_ver][pos_hor] == "." or grid[pos_ver][pos_hor] == chr(i + 65) else "?"

  return "\n".join(["".join(row) for row in grid[::-1]])


def get_supporting_bricks(brick: list, bricks: list) -> list:
  supporting_bricks = []
  brick_positions = get_brick_cells(brick)

  for other_brick in bricks:
    if other_brick == brick:
      continue
    other_brick_positions = get_brick_cells(other_brick)
    for pos in brick_positions:
      if (pos[0], pos[1], pos[2] - 1) in other_brick_positions:
        supporting_bricks.append(other_brick)
        break
  return supporting_bricks


def is_on_ground(brick: list) -> bool:
  brick_positions = get_brick_cells(brick)
  for pos in brick_positions:
    if pos[2] == 1:
      return True
  return False


def settle_bricks(bricks: list) -> list:
  to_settle = True
  settled_bricks = bricks.copy()
  while to_settle:
    to_settle = False
    settling_bricks = []
    for brick in settled_bricks:
      supporting_bricks = get_supporting_bricks(brick, settled_bricks)
      if len(supporting_bricks) > 0 or is_on_ground(brick):
        settling_bricks.append(brick)
      else:
        to_settle = True
        settling_bricks.append([(brick[0][0], brick[0][1], brick[0][2] - 1), (brick[1][0], brick[1][1], brick[1][2] - 1)])

    settled_bricks = settling_bricks.copy()
  return settled_bricks


input_file = open(file_name, 'r')
bricks = [[tuple([int(pos) for pos in coords.split(",")]) for coords in line.split("~")] for line in input_file.read().rstrip().split('\n')]

sorted_bricks = sort_bricks(bricks)
settled_bricks = settle_bricks(bricks)

string_bricks_x = plot_bricks(settled_bricks[0:26], "x")
string_bricks_y = plot_bricks(settled_bricks[0:26], "y")
string_bricks_x_y = plot_bricks(settled_bricks[0:26], "x", "y")
print()
print(string_bricks_x)
print()
print(string_bricks_y)
print()
# print(string_bricks_x_y)

None
