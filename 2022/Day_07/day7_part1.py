def add_to_tree(tree: map, directory: list, file: str, size: int = None):
  current_contents = tree
  for folder in directory:
    if folder in current_contents.keys():
      current_contents = current_contents[folder]
    else:
      current_contents[folder] = {}
      current_contents = current_contents[folder]
  
  if size:
    current_contents[file] = int(size)
  elif file in current_contents.keys():
    pass
  else:
    current_contents[file] = {}


def get_sizes(contents: map, current_directory: list, size_map: map):
  size = 0
  for key, value in contents.items():
    if isinstance(value, int):
      size += value
    else:
      size += get_sizes(value, current_directory + [key], size_map)
  
  size_map[str(current_directory)] = size
  return size 


input_file = open('input.txt', 'r')
commands = [line[1:] for line in input_file.read().rstrip()[1:].split('\n$')]

file_system = {"/": {}}
current_directory = []

for command in commands:
  if command[0:2] == "cd":
    dest = command[3:]
    if dest == "/":
      current_directory = ["/"]
    elif dest == "..":
      current_directory = current_directory[:-1]
    else:
      current_directory.append(dest)
  
  if command[0:2] == "ls":
    contents = command.split('\n')[1:]
    for content in contents:
      file = content.split(" ")
      add_to_tree(file_system, current_directory, file[1], file[0] if file[0] != "dir" else None)


size_map = {}
get_sizes(file_system["/"], ["/"], size_map)

cap = 100000
under_values = [value for value in size_map.values() if value < cap]
print(f"The sum of the folders under {cap} is {sum(under_values)}")

