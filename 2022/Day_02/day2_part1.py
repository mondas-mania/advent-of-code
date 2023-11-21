matching = {
  'A': 'X',
  'B': 'Y',
  'C': 'Z'
}

score_dict = {
  'X': 1,
  'Y': 2,
  'Z': 3
}

def get_victor(round: list):
  if round[0] == round[1]:
    return 0.5
  elif round[0] == 'X':
    return 1 if round[1] == 'Y' else 0
  elif round[0] == 'Y':
    return 1 if round[1] == 'Z' else 0
  elif round[0] == 'Z':
    return 1 if round[1] == 'X' else 0
  else:
    return None

def get_score(round: list):
  victor = get_victor(round)
  return int(6*victor) + score_dict[round[1]]


input_file = open('input.txt', 'r')
rounds = [[matching[round[0]], round[1]]for round in [line.split(' ') for line in input_file.read().strip().split('\n')]]
scores = [get_score(round) for round in rounds]
print(scores)
total_score = sum(scores)
print(f"The total score is {total_score}")