input_file = open('input.txt', 'r')
input_text = input_file.read().rstrip().split('\n\n')

stacks_text = input_text[0].split('\n')
stacks_chars = [list(line) for line in stacks_text[:-1]]
no_stacks = max([int(chars) for chars in stacks_text[-1].split(' ')  if chars != ''])
tallest_stack = len(stacks_chars)
stacks = [[stacks_chars[row_no][(stack_no*4)+1] for row_no in reversed(range(tallest_stack)) if stacks_chars[row_no][(stack_no*4)+1] != ' '] for stack_no in range(no_stacks)]

instructions = input_text[1].split('\n')
instructions_split = [[int(instruction.split(' ')[1]), int(instruction.split(' ')[3]) -1, int(instruction.split(' ')[5]) -1] for instruction in instructions]

for instruction in instructions_split:
  start_stack = instruction[1]
  end_stack = instruction[2]
  to_move = instruction[0]
  for _ in range(to_move):
    stacks[end_stack].append(stacks[start_stack].pop())

top_boxes = [stack[-1] for stack in stacks]
top_boxes_str = ''.join(top_boxes)
print(top_boxes_str)