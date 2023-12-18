file_name = "input_test.txt"

def is_valid_pos(pos: tuple, loss_map: list) -> bool:
  max_row = len(loss_map)
  max_col = len(loss_map[0])
  return (pos[0] >= 0 and pos[1] >= 0) and (pos[0] < max_row and pos[1] < max_col)


def can_go_straight(path: list) -> int:
  # if all of the last 3 cols or rows are equal then can't go straight
  # can always go straight if there's fewer than 3 steps though
  last_three = path[-3:]
  rows = [pos[0] for pos in last_three]
  cols = [pos[1] for pos in last_three]

  return (len(set(rows)) > 1 and len(set(cols)) > 1) or len(last_three) < 3


def get_possible_neighbours(path: list, loss_map: list) -> list:
  # get possible neighbours that are:
  # 1. on the grid and not an invalid index
  # 2. aren't the previous pos
  # 3. not forward if 3 straights
  current_pos = path[-1]
  row = current_pos[0]
  col = current_pos[1]
  possible_neighbours = [potential for potential in [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)] if is_valid_pos(potential, loss_map) and potential not in path]
  straight_allowed = can_go_straight(path)

  if not straight_allowed:
    prev_pos = path[-2]
    if prev_pos[0] == row:
      # remove straight forward if we've got the same rows
      [possible_neighbours.remove(potential) for potential in possible_neighbours if potential[0] == row]
    elif prev_pos[1] == col:
      # remove straight forward if we've got the same cols
      [possible_neighbours.remove(potential) for potential in possible_neighbours if potential[1] == col]
    else:
      print(f"What has happened here? {prev_pos} {current_pos}")

  return possible_neighbours


def get_heat_loss(path: list, loss_map: list) -> int:
  heat_loss = sum([loss_map[pos[0]][pos[1]] for pos in path])
  return heat_loss


def find_best_path(start_pos: tuple, end_pos: list, loss_map: list) -> list:
  best_path = []
  lowest_loss = -1
  paths = [[start_pos]]

  # far too unoptimized
  # if i store visited nodes that can cull it but i'd need to track directions
  # then again the direction won't massively matter
  # map of pos: lowest heat loss?

  while len(paths) > 0:
    new_paths = []

    for path in paths:
      neighbours = get_possible_neighbours(path, loss_map)
      for neighbour in neighbours:
        new_path = path.copy()
        new_path.append(neighbour)
        heat_loss = get_heat_loss(new_path, loss_map)
        if lowest_loss == -1 or heat_loss < lowest_loss:
          if neighbour == end_pos:
            best_path = new_path
            lowest_loss = heat_loss
          else:
            new_paths.append(new_path)

    paths = new_paths  

  return best_path
  pass

input_file = open(file_name, 'r')
loss_dot_jpeg = [[int(val) for val in list(line)] for line in input_file.read().rstrip().split('\n')]

starting_pos = (0,0)
end_pos = (len(loss_dot_jpeg) - 1, len(loss_dot_jpeg[0]) - 1)

test_path = [(0,0), (1,0), (1,1)]
x = get_possible_neighbours(test_path, loss_dot_jpeg)

y = find_best_path(starting_pos, end_pos, loss_dot_jpeg)
None