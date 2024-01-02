file_name = "input.txt"
start = "broadcaster"
no_pushes = 1000

def count_pulses(all_pulses: list) -> tuple:
  low_pulses = len([pulse for pulse in all_pulses if pulse[1] == "low"])
  high_pulses = len([pulse for pulse in all_pulses if pulse[1] == "high"])
  return (low_pulses, high_pulses)


def push_the_button_by_the_sugababes(start_module: str, configuration: dict, no_pushes: int = 1) -> list:
  flip_flops = {k[1:]: False for k in configuration.keys() if "%" in k}
  conjunctions = {k[1:]: {j[1:]: "low" for j in configuration.keys() if k[1:] in configuration[j]} for k in configuration.keys() if "&" in k}
  all_pulses = []

  for _ in range(no_pushes):
    all_pulses += [("button", "low", start_module)]
    current_inputs = [ (start_module, "low", module) for module in configuration[start_module] ]

    while len(current_inputs) > 0:
      all_pulses += current_inputs
      new_inputs = []

      for input in current_inputs:
        origin = input[0]
        strength = input[1]
        dest = input[2]
        
        if dest in flip_flops:
          if strength == "high":
            continue
          else:
            if flip_flops[dest]:
              flip_flops[dest] = False
              new_inputs += [(dest, "low", new_dest) for new_dest in configuration[f"%{dest}"]]
            else:
              flip_flops[dest] = True
              new_inputs += [(dest, "high", new_dest) for new_dest in configuration[f"%{dest}"]]
        elif dest in conjunctions:
          conjunctions[dest][origin] = strength
          if all([stren == "high" for stren in conjunctions[dest].values()]):
            new_inputs += [(dest, "low", new_dest) for new_dest in configuration[f"&{dest}"]]
          else:
            new_inputs += [(dest, "high", new_dest) for new_dest in configuration[f"&{dest}"]]
        else:
          print(f"{strength} pulse sent to {dest}")

      current_inputs = new_inputs

  return all_pulses


input_file = open(file_name, 'r')
configuration = {line.split(" -> ")[0]: line.split(" -> ")[1].split(", ") for line in input_file.read().rstrip().split('\n')}
pulses = push_the_button_by_the_sugababes(start, configuration, no_pushes)
pulse_counts = count_pulses(pulses)

print(f"The total pulse value is {pulse_counts[0]} low x {pulse_counts[1]} high = {pulse_counts[0] * pulse_counts[1]}")
