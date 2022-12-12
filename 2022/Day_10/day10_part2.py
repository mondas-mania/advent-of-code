input_file = open('input.txt', 'r')
instructions = [None if instruction == "noop" else int(instruction.split(' ')[1]) for instruction in input_file.read().rstrip().split('\n')]

x_register = [1]
for instruction in instructions:
  x_register.append(x_register[-1])
  if instruction is None:
    pass
  else:
    x_register.append(x_register[-1] + instruction)

monitor_string = ""
for i in range(len(x_register) - 1):
  pos = i % 40
  if x_register[i] in range(pos - 1, pos + 2):
    monitor_string += "#"
  else:
    monitor_string += "."

for i in range(0,len(monitor_string), 40):
  print(monitor_string[i:i+40])