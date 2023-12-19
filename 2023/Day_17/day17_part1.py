file_name = "input.txt"

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

def get_str_pos(pos: tuple) -> str:
  return ",".join([str(pos[0]), str(pos[1])])


def find_best_path(start_pos: tuple, end_pos: list, loss_map: list) -> list:
  best_path = []
  paths = [[start_pos]]

  visited = {
    get_str_pos(start_pos): loss_map[start_pos[0]][start_pos[1]]
  }

  while len(paths) > 0:
    new_paths = []

    for path in paths:
      neighbours = get_possible_neighbours(path, loss_map)
      for neighbour in neighbours:
        new_path = path.copy()
        new_path.append(neighbour)
        heat_loss = get_heat_loss(new_path, loss_map)

        str_neighbour = get_str_pos(neighbour)
        if str_neighbour in visited:
          if heat_loss > visited[str_neighbour]:
            continue

        visited[str_neighbour] = heat_loss

        if neighbour == end_pos:
          best_path = new_path
        else:
          new_paths.append(new_path)

    paths = new_paths  

  return best_path


input_file = open(file_name, 'r')
loss_dot_jpeg = [[int(val) for val in list(line)] for line in input_file.read().rstrip().split('\n')]

starting_pos = (0,0)
end_pos = (len(loss_dot_jpeg) - 1, len(loss_dot_jpeg[0]) - 1)

best_path = find_best_path(starting_pos, end_pos, loss_dot_jpeg)
lowest_loss = get_heat_loss(best_path, loss_dot_jpeg)

print(f"\nThe least heat loss possible is {lowest_loss}")

depiction = ''.join([''.join(["#" if (row, col) in best_path else "." for col in range(len(loss_dot_jpeg[0]))] + ["\n"]) for row in range(len(loss_dot_jpeg))])
print(f"{depiction}")
None