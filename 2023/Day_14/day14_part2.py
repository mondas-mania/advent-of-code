file_name = "input_test.txt"

def rotate_dish_clockwise(dish: list) -> list:
  dish_size = len(dish)
  new_dish = []
  for i, row in enumerate(dish):
    new_row = []
    for j in range(len((row))):
      new_row.append(dish[j][dish_size - 1 - i])
    new_dish.append(new_row)
  return new_dish

def rotate_dish_anticlockwise(dish: list) -> list:
  dish_size = len(dish[0])
  new_dish = []
  for i, row in enumerate(dish):
    new_row = []
    for j in range(len(row)):
      new_row.append(dish[dish_size - 1 - j][i])
    new_dish.append(new_row)
  return new_dish

def copy_dish(dish: list) -> list:
  new_dish = []
  for row in dish:
    new_dish.append(row.copy())
  return new_dish

def get_load(dish: list) -> int:
  num_rows = len(dish)
  total = 0
  for i, row in enumerate(dish):
    row_total = sum([(num_rows - i) for value in row if value == "O"])
    total += row_total
  return total

def spin_cycle(dish: list) -> list:
  for _ in range(4):
    dish = tilt(dish)
    dish = rotate_dish_anticlockwise(dish)
  return dish

def tilt(dish: list) -> list:
  has_tilted = False
  dish_copy = copy_dish(dish)
  for i in range(1, len(dish_copy)):
    for j, value in enumerate(dish_copy[i]):
      if value == "O" and dish_copy[i-1][j] == ".":
        dish_copy[i-1][j] = "O"
        dish_copy[i][j] = "."
        has_tilted = True
  
  if not has_tilted:
    return dish
  else:
    return tilt(dish_copy)

input_file = open(file_name, 'r')
dish = [list(line) for line in input_file.read().rstrip().split('\n')]

spun_dish = copy_dish(dish)
for i in range(1000000000):
  original_spun_dish = copy_dish(spun_dish)
  spun_dish = spin_cycle(spun_dish)
  if original_spun_dish == spun_dish:
    print(f"Breaking after {i} iterations")
    break


total = get_load(spun_dish)

print(f"The total load on the north-tilted dish is {total}")

None