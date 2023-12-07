file_name = "input.txt"
max_cubes = {
  "red": 12,
  "green": 13,
  "blue": 14
}

input_file = open(file_name, 'r')
lines = [line for line in input_file.read().rstrip().split('\n')]
games = [[int(line[5:line.find(":")]), [[draw.split(" ") for draw in observation.split(", ")] for observation in line[line.find(":") + 2:].split("; ")]] for line in lines]
feasible = [[int(game[0]), all([all([int(colour[0]) <= max_cubes[colour[1]] for colour in handful]) for handful in game[1]])] for game in games]
print(feasible)
game_sum = sum([evaluation[0] if evaluation[1] else 0 for evaluation in feasible])
print(f"The sum of game IDs is {game_sum}.")