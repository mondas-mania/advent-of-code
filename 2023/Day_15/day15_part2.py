file_name = "input.txt"

def get_hash(hash: str) -> int:
  current_value = 0
  for char in list(hash):
    current_value = current_value + ord(char)
    current_value = current_value * 17
    current_value = current_value % 256
  return current_value


def calculate_focusing_power(box: dict) -> int:
  focusing_power = 0
  order = box["ORDER"]
  for i, label in enumerate(order):
    focusing_power += (i + 1) * box[label] * (box["BOX_NO"] + 1)
  return focusing_power


def dash_operator(label: str, boxes: list) -> list:
  box_index = get_hash(label)
  if label in boxes[box_index]:
    boxes[box_index]["ORDER"].remove(label)
    del boxes[box_index][label]
  return boxes


def eq_operator(label: str, value: int, boxes: list) -> list:
  box_index = get_hash(label)
  if label in boxes[box_index]:
    boxes[box_index][label] = value
  else:
    boxes[box_index][label] = value
    boxes[box_index]["ORDER"] = boxes[box_index]["ORDER"] + [label]

  return boxes


def carry_out_step(step: str, boxes: list) -> list:
  if "-" in step:
    label, _ = step.split("-")
    boxes = dash_operator(label, boxes)
  else:
    label, value = step.split("=")
    value = int(value)
    boxes = eq_operator(label, value, boxes)
  return boxes


def get_boxes(sequences: list) -> list:
  boxes = [{"ORDER": [], "BOX_NO": i} for i in range(256)]
  for step in sequences:
    boxes = carry_out_step(step, boxes)
  return boxes


def get_total_focusing_power(boxes: list) -> int:
  focusing_powers = [calculate_focusing_power(box) for box in boxes]
  return sum(focusing_powers)


input_file = open(file_name, 'r')
init_seq = (input_file.read().rstrip().split('\n')[0]).split(",")

boxes = get_boxes(init_seq)

total = get_total_focusing_power(boxes)
print(f"The sum of all the focusing powers is {total}")
