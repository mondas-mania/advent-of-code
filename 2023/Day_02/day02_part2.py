import numpy

file_name = "input.txt"

def get_max_cubes(observations: list) -> dict:
  max_dict = {}
  for handful in observations:
    for colour in handful:
      if colour[1] not in max_dict.keys() or max_dict[colour[1]] < int(colour[0]):
        max_dict[colour[1]] = int(colour[0])
  return max_dict

input_file = open(file_name, 'r')
lines = [line for line in input_file.read().rstrip().split('\n')]
games = [[int(line[5:line.find(":")]), [[draw.split(" ") for draw in observation.split(", ")] for observation in line[line.find(":") + 2:].split("; ")]] for line in lines]
max_cubes = [[game[0], get_max_cubes(game[1])] for game in games]
powers = [[game[0], numpy.prod(list(game[1].values()))] for game in max_cubes]
print(f"The sum of powers is {sum([power[1] for power in powers])}.")