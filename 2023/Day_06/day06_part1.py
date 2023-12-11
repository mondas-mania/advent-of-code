import numpy

file_name = "input.txt"

def return_distance(time: int, total_time: int) -> int:
  return time * (total_time - time)

input_file = open(file_name, 'r')
lines = [[element for element in line.split(" ") if element != ''] for line in input_file.read().rstrip().split('\n')]
time_distance_pairs = [(int(lines[0][i]), int(lines[1][i])) for i in range(1, len(lines[0]))]
better_distances = [[return_distance(t, td_pair[0]) for t in range(td_pair[0] + 1) if return_distance(t, td_pair[0]) > td_pair[1]] for td_pair in time_distance_pairs]

print(f"The product of all better distances is {numpy.prod([len(distances) for distances in better_distances])}")
None