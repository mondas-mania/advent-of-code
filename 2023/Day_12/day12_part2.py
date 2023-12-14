file_name = "input_test.txt"

def get_contiguous_count(springs: list, pos: int) -> int:
  cut_list = springs[pos:]
  counter = 0
  for i in range(len(cut_list)):
    if cut_list[i] != cut_list[0]:
      return counter
    counter += 1
  return counter

def get_contiguous_list(springs: list) -> list:
  contiguous_counts = []
  pos = 0
  while pos < len(springs):
    if springs[pos] in [".", "?"]:
      pos += 1
      continue
    else:
      count = get_contiguous_count(springs, pos)
      contiguous_counts.append(count)
      pos += count
  return contiguous_counts

def evaluate_configuration(springs: list, target: list) -> bool:
  # Evaluate if a list of springs is valid against the target
  contiguous_counts = get_contiguous_list(springs)
  evaluation = contiguous_counts == target
  return evaluation

def get_spring_permuation(springs: list) -> list:
  if "?" not in springs:
    return [springs]
  
  spring_permutations = []
  for potential in [".", "#"]:
    new_springs = springs.copy()
    pos = new_springs.index("?")
    new_springs[pos] = potential
    spring_permutations += get_spring_permuation(new_springs)
  
  return spring_permutations

def unfold_map(spring_values: list) -> list:
  springs = spring_values[0]
  counts = spring_values[1]
  new_springs = ((springs + ["?"]) * 5)[:-1]
  new_counts = counts * 5
  return [new_springs, new_counts]


input_file = open(file_name, 'r')
spring_values = [[list(line.split(" ")[0]), [int(num) for num in line.split(" ")[1].split(",")]] for line in input_file.read().rstrip().split('\n')]

unfolded_values = [unfold_map(spring_value) for spring_value in spring_values]

spring_permutations = [get_spring_permuation(values[0]) for values in unfolded_values]
valid_permutations = [[permutation for permutation in spring_permutations[i] if evaluate_configuration(permutation, unfolded_values[i][1])] for i in range(len(unfolded_values))]
print(f"There are {sum([len(permutations) for permutations in valid_permutations])} possible arrangements in total.")
None