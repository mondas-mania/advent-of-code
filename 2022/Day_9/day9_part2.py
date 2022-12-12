def get_rope_length(head_pos: tuple, tail_pos: tuple):
  x_dist = head_pos[0] - tail_pos[0]
  y_dist = head_pos[1] - tail_pos[1]
  length = max(abs(x_dist), abs(y_dist))
  if x_dist > 0:
    change_x = 1
  elif x_dist < 0:
    change_x = -1
  else:
    change_x = 0

  if y_dist > 0:
    change_y = 1
  elif y_dist < 0:
    change_y = -1
  else:
    change_y = 0


  return length, change_x, change_y

def get_tail_positions(rope: list, movement: tuple):
  direction = movement[0]
  new_tail_history = []
  for _ in range(movement[1]):
    head_pos = rope[0]
    if direction == "U":
      rope[0] = (head_pos[0], head_pos[1] + 1)
    elif direction == "R":
      rope[0] = (head_pos[0] + 1, head_pos[1])
    elif direction == "D":
      rope[0] = (head_pos[0], head_pos[1] - 1)
    elif direction == "L":
      rope[0] = (head_pos[0] - 1, head_pos[1])
    else:
      print(f"Something's gone wrong here, Movement: {movement}")

    for i in range(1, len(rope)):
      knot_pos = rope[i]
      delta, change_x, change_y = get_rope_length(rope[i-1], rope[i])
      if delta <= 1:
        pass
      else:
        rope[i] = (knot_pos[0] + change_x, knot_pos[1] + change_y)

    new_tail_history.append(rope[-1])
  
  return new_tail_history

input_file = open('input.txt', 'r')
movements = [(movement.split(' ')[0], int(movement.split(' ')[1])) for movement in input_file.read().rstrip().split('\n')]

rope_length = 10
rope = [(0,0) for _ in range(rope_length)]
tail_history = [rope[-1]]

for movement in movements:
  # Head and Tail positions will update in place
  new_tail_history = get_tail_positions(rope, movement)
  tail_history += new_tail_history

print(f"The tail visited {len(set(tail_history))} different tiles")