file_name = "input.txt"

def transpose_grid(grid: list) -> list:
  new_grid = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]
  return new_grid

def get_mirror_rows(grid: list) -> tuple:
  index = 1 # need to have a line above at least
  while index < len(grid):

    max_diff = min(index, len(grid) - index)
    rows_before = grid[index - max_diff:index][::-1]
    rows_after = grid[index: index + max_diff]
    if rows_before == rows_after:
      return (index - 1, index)
    index += 1

  return None


def get_horizontal_reflection(grid: list) -> tuple:
  transposed_grid = transpose_grid(grid)
  return get_mirror_rows(transposed_grid)

def get_vertical_reflection(grid: list) -> tuple:
  return get_mirror_rows(grid)

def get_all_reflections(grids: list) -> dict:
  horizontal_reflections = [get_horizontal_reflection(grid) for grid in grids]
  vertical_reflections = [get_vertical_reflection(grid) for grid in grids]

  culled_horizontal_reflections = [reflection for reflection in horizontal_reflections if reflection]
  culled_vertical_reflections = [reflection for reflection in vertical_reflections if reflection]

  return {
    "horizontal": culled_horizontal_reflections,
    "vertical": culled_vertical_reflections
  }

def summarize(reflections: dict) -> int:
  rows_above = [100 * boundary[1] for boundary in reflections["vertical"]]
  rows_left = [boundary[1] for boundary in reflections["horizontal"]]
  return sum(rows_above) + sum(rows_left)


input_file = open(file_name, 'r')
grids = [[list(line) for line in grid.split("\n")] for grid in input_file.read().rstrip().split('\n\n')]

reflections = get_all_reflections(grids)
total = summarize(reflections)

print(f"The summary of all mirrors is {total}")

None