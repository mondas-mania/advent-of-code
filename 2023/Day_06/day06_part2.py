file_name = "input.txt"

def return_distance(time: int, total_time: int) -> int:
  return time * (total_time - time)

def is_better_distance(time: int, total_time: int, previous_time: int) -> int:
  dist = return_distance(time, total_time)
  return 1 if dist > previous_time else 0

input_file = open(file_name, 'r')
lines = [line.replace(" ", "").split(":") for line in input_file.read().rstrip().split('\n')]
time_distance_pair = (int(lines[0][1]), int(lines[1][1]))
better_distances = [is_better_distance(t, time_distance_pair[0], time_distance_pair[1]) for t in range(time_distance_pair[0] + 1)]

print(f"The count of all better distances is {sum(better_distances)}")
None
 