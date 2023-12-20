file_name = "input.txt"
start_pos = (0,0)


def get_str_cell(pos: tuple) -> str:
  return ",".join([str(num) for num in pos])


def get_boundary_points(instructions: list, starting_pos: tuple) -> dict:
  boundaries = []
  current_pos = starting_pos

  for instruction in instructions:
    dir = instruction[0].split(" ")[0]
    length = int(instruction[0].split(" ")[1])
    hex = instruction[1]

    match dir:
      case "R":
        new_pos = (current_pos[0], current_pos[1] + length)
        boundaries.append(new_pos)
        current_pos = new_pos
      case "U":
        new_pos = (current_pos[0] - length, current_pos[1])
        boundaries.append(new_pos)
        current_pos = new_pos
      case "L":
        new_pos = (current_pos[0], current_pos[1] - length)
        boundaries.append(new_pos)
        current_pos = new_pos
      case "D":
        new_pos = (current_pos[0] + length, current_pos[1])
        boundaries.append(new_pos)
        current_pos = new_pos
      case _:
        print(f"Unknown dir: {dir}")
  
  return boundaries


def dig_trench(instructions: list, starting_pos: tuple) -> dict:
  dug_spots = {}
  current_pos = starting_pos

  for instruction in instructions:
    dir = instruction[0].split(" ")[0]
    length = int(instruction[0].split(" ")[1])
    hex = instruction[1]

    match dir:
      case "R":
        new_pos = [(current_pos[0], current_pos[1] + i) for i in range(1, length + 1)]
        dug_spots.update({get_str_cell(pos): hex for pos in new_pos })
        current_pos = new_pos[-1]
      case "U":
        new_pos = [(current_pos[0] - i, current_pos[1]) for i in range(1, length + 1)]
        dug_spots.update({get_str_cell(pos): hex for pos in new_pos })
        current_pos = new_pos[-1]
      case "L":
        new_pos = [(current_pos[0], current_pos[1] - i) for i in range(1, length + 1)]
        dug_spots.update({get_str_cell(pos): hex for pos in new_pos })
        current_pos = new_pos[-1]
      case "D":
        new_pos = [(current_pos[0] + i, current_pos[1]) for i in range(1, length + 1)]
        dug_spots.update({get_str_cell(pos): hex for pos in new_pos })
        current_pos = new_pos[-1]
      case _:
        print(f"Unknown dir: {dir}")
  
  return dug_spots


def get_inner_spots(boundaries: list) -> int:
  anticlockwise = boundaries[::-1]
  shoelaced = [anticlockwise[i-1][0] * anticlockwise[i][1] - anticlockwise[i][0] * anticlockwise[i-1][1] for i in range(1, len(anticlockwise))]
  summed_shoelace = int(0.5 * sum(shoelaced))
  return summed_shoelace


input_file = open(file_name, 'r')
instructions = [[segment[:-1] for segment in line.split('(')] for line in input_file.read().rstrip().split('\n')]

dug_trench = dig_trench(instructions, start_pos)
boundaries_clockwise = get_boundary_points(instructions, start_pos)
inner_spots = get_inner_spots(boundaries_clockwise)

total = inner_spots + int(0.5 * len(dug_trench.keys())) + 1
print(f"The total amount of lava that can fit is {total} meters cubed")
