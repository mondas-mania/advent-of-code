file_name = "input.txt"
seed_conversion_maps = {}

def get_destination_value(conversion_list: list, input: int) -> int:
  destination_value = input
  for conversion in conversion_list:
    dst = conversion[0]
    src = conversion[1]
    rng = conversion[2]
    if input in range(src, src + rng):
      offset = input - src
      destination_value = dst + offset
      return destination_value
  return destination_value

def get_next_step(dst: str, keys: list):
  for key in keys:
    new_src = key.split("-to-")[0]
    if dst == new_src:
      return key
  return None

def get_next_steps(almanacs: dict):
  next_steps_dict = {}
  next_steps_dict["seed"] = get_next_step("seed", list(almanacs.keys()))
  for conversion in list(almanacs.keys()):
    dst = conversion.split("-to-")[1]
    next_steps_dict[conversion] = get_next_step(dst, list(almanacs.keys()))
  return next_steps_dict

def src_to_dst(almanacs: dict, next_steps: dict, source_key: str, input_value: int, original_value: int) -> int:
  if original_value not in seed_conversion_maps.keys():
    seed_conversion_maps[original_value] = {source_key: original_value}
  else:
    seed_conversion_maps[original_value][source_key.split("-to-")[1]] = input_value

  if next_steps[source_key] is None:
    return input_value
  
  next_step = next_steps[source_key]
  almanac = almanacs[next_step]
  destination_value = get_destination_value(almanac, input_value)
  return src_to_dst(almanacs, next_steps, next_step, destination_value, original_value)




input_file = open(file_name, 'r')
lines = [line for line in input_file.read().rstrip().split('\n\n')]
seeds = [int(value) for value in lines[0].split(":")[1].strip().split(" ")]
almanacs = {map.split(":")[0].replace("map", "").strip(): [[int(value) for value in line.split(" ")] for line in map.split(":")[1].split("\n")[1:]] for map in lines[1:]}
next_steps_dict = get_next_steps(almanacs)

seeds_to_locations = {seed: src_to_dst(almanacs, next_steps_dict, "seed", seed, seed) for seed in seeds}
closest_loc = sorted(seeds_to_locations.items(), key=lambda x: x[1])[0]

print(f"The closest location is {closest_loc[1]} which corresponds to initial seed {closest_loc[0]}.")
None