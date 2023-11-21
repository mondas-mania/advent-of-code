def get_rope_length(head_pos: tuple, tail_pos: tuple):
  x_dist = abs(head_pos[0] - tail_pos[0])
  y_dist = abs(head_pos[1] - tail_pos[1])
  return max(x_dist, y_dist)

def get_tail_positions(head_pos: tuple, tail_pos: tuple, movement: tuple):
  direction = movement[0]
  new_tail_history = []
  for i in range(movement[1]):
    prev_head = (head_pos[0], head_pos[1])
    if direction == "U":
      head_pos = (head_pos[0], head_pos[1] + 1)
    elif direction == "R":
      head_pos = (head_pos[0] + 1, head_pos[1])
    elif direction == "D":
      head_pos = (head_pos[0], head_pos[1] - 1)
    elif direction == "L":
      head_pos = (head_pos[0] - 1, head_pos[1])
    else:
      print(f"Something's gone wrong here, Movement: {movement}")

    if get_rope_length(head_pos, tail_pos) <= 1:
      pass
    else:
      tail_pos = (prev_head[0], prev_head[1])
    new_tail_history.append(tail_pos)
    
  return head_pos, tail_pos, new_tail_history

input_file = open('input.txt', 'r')
movements = [(movement.split(' ')[0], int(movement.split(' ')[1])) for movement in input_file.read().rstrip().split('\n')]

head_pos = (0, 0)
tail_pos = (0, 0)
tail_history = [tail_pos]

for movement in movements:
  head_pos, tail_pos, new_tail_history = get_tail_positions(head_pos, tail_pos, movement)
  tail_history += new_tail_history

print(f"The tail visited {len(set(tail_history))} different tiles")