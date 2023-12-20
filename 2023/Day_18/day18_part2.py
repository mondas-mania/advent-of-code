file_name = "input.txt"
start_pos = (0,0)

dir_map = {
  "0": "R",
  "1": "D",
  "2": "L",
  "3": "U"
}


def get_str_cell(pos: tuple) -> str:
  return ",".join([str(num) for num in pos])


def get_boundary_points(instructions: list, starting_pos: tuple) -> dict:
  boundaries = []
  current_pos = starting_pos

  for instruction in instructions:
    dir = instruction[0]
    length = instruction[1]

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
  dug_spots = []
  current_pos = starting_pos

  for instruction in instructions:
    dir = instruction[0]
    length = instruction[1]

    match dir:
      case "R":
        new_pos = [(current_pos[0], current_pos[1] + i) for i in range(1, length + 1)]
        dug_spots += new_pos
        current_pos = new_pos[-1]
      case "U":
        new_pos = [(current_pos[0] - i, current_pos[1]) for i in range(1, length + 1)]
        dug_spots += new_pos
        current_pos = new_pos[-1]
      case "L":
        new_pos = [(current_pos[0], current_pos[1] - i) for i in range(1, length + 1)]
        dug_spots += new_pos
        current_pos = new_pos[-1]
      case "D":
        new_pos = [(current_pos[0] + i, current_pos[1]) for i in range(1, length + 1)]
        dug_spots += new_pos
        current_pos = new_pos[-1]
      case _:
        print(f"Unknown dir: {dir}")
  
  return dug_spots


def get_inner_spots(boundaries: list) -> int:
  anticlockwise = boundaries[::-1]
  shoelaced = [anticlockwise[i-1][0] * anticlockwise[i][1] - anticlockwise[i][0] * anticlockwise[i-1][1] for i in range(1, len(anticlockwise))]
  summed_shoelace = int(0.5 * sum(shoelaced))
  return summed_shoelace


def get_new_instructions(old_instructions: list) -> list:
  new_instructions = [(dir_map[instruction[-1]], int(instruction[:5], 16)) for instruction in instructions]
  return new_instructions


input_file = open(file_name, 'r')
instructions = [line.split('(')[1][1:-1] for line in input_file.read().rstrip().split('\n')]
new_instructions = get_new_instructions(instructions)

dug_trench = dig_trench(new_instructions, start_pos)
boundaries_clockwise = get_boundary_points(new_instructions, start_pos)
inner_spots = get_inner_spots(boundaries_clockwise)

total = inner_spots + int(0.5 * len(dug_trench)) + 1
print(f"The total amount of lava that can fit is {total} meters cubed")
