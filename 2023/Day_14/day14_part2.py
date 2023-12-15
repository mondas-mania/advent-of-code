file_name = "input.txt"

def rotate_dish_clockwise(dish: list) -> list:
  dish_size = len(dish)
  new_dish = [[dish[j][dish_size - 1 - i] for j in range(len(dish[i]))] for i in range(dish_size)]
  return new_dish

def rotate_dish_anticlockwise(dish: list) -> list:
  dish_size = len(dish[0])
  new_dish = [[dish[dish_size - 1 - j][i] for j in range(len(dish[i]))] for i in range(dish_size)]
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
shorter_spins = 150
full_spins = 1000000000
loads = []
loop_length = 0
loop_start = 0
loop = []

# The loads begin to loop after a while so best to record them all
# in a much smaller sample size (150 is arbitrary in this case)
# as 1000000000 cycles is not at all feasible
for i in range(shorter_spins):
  original_spun_dish = copy_dish(spun_dish)
  spun_dish = spin_cycle(spun_dish)
  loads.append(get_load(spun_dish))

# We need to identify the length of the loop starting from the end of the recorded loads
for i in range(1, int(shorter_spins/2)):
  if loads[-i:] == loads[-i * 2:-i]:
    print(f"Loop at {i} of \n {loads[-i * 2:-i]} ")
    loop_length = i
    break

# Once we have a length we can determine the start of the loop 
# (it doesn't begin looping for a while),
# and determine the full loop itself
for i in range(1, int(shorter_spins - loop_length)):
  if loads[i:i+loop_length] == loads[i+loop_length: i+(loop_length*2)]:
    loop = loads[i: i+loop_length]
    loop_start = i
    break

# Using this loop we can project that forward to its position
# with 1000000000 spin cycles
pos = ((full_spins - loop_start) % loop_length) - 1
final_total = loop[pos]

print(f"The final total load on the north-tilted dish is {final_total}")
