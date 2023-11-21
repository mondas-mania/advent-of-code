victory_dict = {
  'X': 0,
  'Y': 3,
  'Z': 6
}

shape_dict = {
  'A': 1,
  'B': 2,
  'C': 3
}

def get_own_shape(opponent_shape: str, victory_points: int):
  if victory_points == 3:
    return opponent_shape
  elif opponent_shape == 'A':
    return 'B' if victory_points == 6 else 'C'
  elif opponent_shape == 'B':
    return 'C' if victory_points == 6 else 'A'
  elif opponent_shape == 'C':
    return 'A' if victory_points == 6 else 'B'
  else:
    return None

def get_score(round: list):
  victory_points = victory_dict[round[1]]
  shape = get_own_shape(round[0], victory_points)
  return victory_points + shape_dict[shape]


input_file = open('input.txt', 'r')
rounds = [line.split(' ') for line in input_file.read().strip().split('\n')]
scores = [get_score(round) for round in rounds]
print(scores)
total_score = sum(scores)
print(f"The total score is {total_score}")