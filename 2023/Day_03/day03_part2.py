file_name = "input.txt"
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_chars = ["*", "-", "+", "/", "&", "$", "=", "@", "#", "%"]
# special_chars derived from below snippet
# input_file = open(file_name, 'r')
# lines = [line for line in input_file.read().rstrip()]
# print(set(lines))

def is_valid(schematic: list, coord: list) -> bool:
  row = coord[0]
  col = coord[1]
  max_row = len(schematic)
  max_col = len(schematic[0])
  is_valid = row < max_row and col < max_col and row >= 0 and col >= 0
  return is_valid


def get_neighbouring_cells(schematic: list, coord: list) -> list:
  row = coord[0]
  col = coord[1]

  possible_neighbours = [
    [row + 1, col], # south
    [row - 1, col], # north
    [row, col + 1], # east
    [row, col - 1], # west
    [row + 1, col + 1], # south east
    [row - 1, col + 1], # north east
    [row + 1, col - 1], # south west
    [row - 1, col - 1], # north west
  ]

  valid_neighbours = []
  for neighbour in possible_neighbours:
    valid_neighbours.append(neighbour) if is_valid(schematic, neighbour) else None

  return valid_neighbours

def parse_full_number(schematic: list, cell: list) -> list:
  row = cell[0]
  col = cell[1]
  max_cols = len(schematic[row])
  full_row = schematic[row]

  full_int_pos = []
  full_int_value = ""

  if full_row[col] not in digits or (col > 0 and full_row[col - 1] in digits):
    return
  
  pos = col
  while pos < max_cols and full_row[pos] in digits:
    full_int_pos.append([row, pos])
    full_int_value += full_row[pos]
    pos += 1

  return [full_int_value, full_int_pos]

def is_part_number(schematic: list, full_int_pos: list):
  all_neighbours = []
  [[all_neighbours.append(neighbour) for neighbour in get_neighbouring_cells(schematic, pos)] for pos in full_int_pos]
  
  for neighbour in all_neighbours:
    if schematic[neighbour[0]][neighbour[1]] in special_chars:
      return True
  return False
  


input_file = open(file_name, 'r')
schematic = [list(line) for line in input_file.read().rstrip().split('\n')]

all_numbers = []
for row in range(len(schematic)):
  for col in range(len(schematic[row])):
    number = parse_full_number(schematic, [row, col])
    all_numbers.append(number) if number is not None else None

all_gears = []
for row in range(len(schematic)):
  for col in range(len(schematic[row])):
    all_gears.append([row, col]) if schematic[row][col] == "*" else None

gear_neighbour_nums = {}
gear_ratios = {}
for gear in all_gears:
  gear_index = str(gear[0]) + "," + str(gear[1])
  gear_neighbour_nums[gear_index] = set()
  neighbours = get_neighbouring_cells(schematic, gear)
  for neighbour in neighbours:
    for number in all_numbers:
      if neighbour in number[1]:
        gear_neighbour_nums[gear_index].add(number[0])
  if len(gear_neighbour_nums[gear_index]) == 2:
    list_ver = list(gear_neighbour_nums[gear_index])
    gear_ratios[gear_index] = int(list_ver[0]) * int(list_ver[1])

print(f"The sum of all gear ratios is {sum(list(gear_ratios.values()))}.")
