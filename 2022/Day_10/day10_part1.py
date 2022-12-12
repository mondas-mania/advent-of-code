input_file = open('input.txt', 'r')
instructions = [None if instruction == "noop" else int(instruction.split(' ')[1]) for instruction in input_file.read().rstrip().split('\n')]
# print(instructions)

x_register = [1]
for instruction in instructions:
  x_register.append(x_register[-1])
  if instruction is None:
    pass
  else:
    x_register.append(x_register[-1] + instruction)

print(f"The sum is {sum([x_register[i-1] * i for i in range(20,len(x_register),40)])}")