file_name = "input.txt"
starting_workflow = "in"

def get_score(part: dict) -> int:
  return sum([val for val in part.values()])

def get_next_step(part: dict, workflow: list) -> str:
  for comparison in workflow:
    if len(comparison) == 1:
      return comparison[0]
    
    comparator = "<" if "<" in comparison[0] else ">"
    letter = comparison[0].split(comparator)[0]
    value = int(comparison[0].split(comparator)[1])
    part_value = part[letter]

    if (comparator == "<" and part_value < value) or (comparator == ">" and part_value > value):
      return comparison[1]
  
  return None

def is_part_accepted(part: dict, workflows: dict, starting_workflow: str) -> bool:
  workflow_key = starting_workflow

  while workflow_key not in ["R", "A"]:
    workflow_key = get_next_step(part, workflows[workflow_key])

  return workflow_key == "A"


input_file = open(file_name, 'r')
workflows_and_parts = [line.split("\n") for line in input_file.read().rstrip().split('\n\n')]
parts = [{rating.split("=")[0]: int(rating.split("=")[1]) for rating in part[1:-1].split(",")}  for part in workflows_and_parts[1]]
workflows = {workflow.split("{")[0]: [ifthen.split(":") for ifthen in workflow.split("{")[1][:-1].split(",")] for workflow in workflows_and_parts[0]}

accepted = [is_part_accepted(part, workflows, starting_workflow) for part in parts]
scores = [get_score(parts[i]) for i in range(len(accepted)) if accepted[i]]

print(f"The total score of accepted parts is {sum(scores)}")
