input_file = open('input.txt', 'r')
monkey_string = [monkey for monkey in input_file.read().rstrip().split('\n\n')]

operations_dict = {}
test_dict = {}
inventory_dict = {}

monkey_dict = {}

for i, monkey in enumerate(monkey_string):
  monkey_info = [info.strip() for info in monkey.split('\n')]
  monkey_dict[i] = {}
  monkey_dict[i]["investigate_count"] = 0
  monkey_dict[i]["inv"] = [int(item) for item in monkey_info[1][15:].split(', ')]
  monkey_dict[i]["op"] = [component for component in monkey_info[2][17:].split(' ')]
  monkey_dict[i]["test"] = {}
  monkey_dict[i]["test"]["q"] = [component for component in monkey_info[3][6:].split(' ')]
  monkey_dict[i]["test"][1] = int(monkey_info[4][25:])
  monkey_dict[i]["test"][0] = int(monkey_info[5][26:])

rounds = 20

for round_no in range(rounds):
  for monkey, monkey_info in monkey_dict.items():
    if len(monkey_info["inv"]) == 0:
      continue

    for item in monkey_info["inv"]:
      monkey_dict[monkey]["investigate_count"] += 1
      value_1 = item if monkey_info["op"][0] == "old" else int(monkey_info["op"][0])
      value_2 = item if monkey_info["op"][2] == "old" else int(monkey_info["op"][2])
      if monkey_info["op"][1] == "+":
        new_worry = value_1 + value_2
      elif monkey_info["op"][1] == "*":
        new_worry = value_1 * value_2
      elif monkey_info["op"][1] == "-":
        new_worry = value_1 - value_2
      elif monkey_info["op"][1] == "/":
        new_worry = value_1 / value_2
      else:
        print(f"Operator {monkey_info['op'][1]} not known")

      new_worry = new_worry // 3

      if monkey_info["test"]["q"][0:2] == ["divisible", "by"]:
        monkey_destination = monkey_info["test"][1] if new_worry % int(monkey_info["test"]["q"][2]) == 0 else monkey_info["test"][0]
      else:
        print(f"Operator {monkey_info['test']['q'][0:2]} is not supported.")
        monkey_destination = None

      monkey_dict[monkey_destination]["inv"].append(new_worry)
      monkey_dict[monkey]["inv"] = monkey_dict[monkey]["inv"][1:]
  print(f"END OF ROUND {round_no+1}: {[[monkey, monkey_info['inv']] for monkey, monkey_info in monkey_dict.items()]}")

sorted_counts = [monkey_info['investigate_count'] for monkey_info in monkey_dict.values()]
sorted_counts.sort()
print(f"The total monkey business is {sorted_counts[-2] * sorted_counts[-1]}")