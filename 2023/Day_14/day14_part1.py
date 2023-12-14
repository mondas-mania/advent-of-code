file_name = "input.txt"

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
tilted_dish = tilt(dish)
total = get_load(tilted_dish)

print(f"The total load on the north-tilted dish is {total}")

None