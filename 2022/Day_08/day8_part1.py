def is_visible(row: int, column: int, forest: list):
  trees_left = forest[row][:column]
  trees_right = forest[row][column+1:]
  trees_above = [forest[i][column] for i in range(0,row)]
  trees_below = [forest[i][column] for i in range(row + 1, len(forest))]
  height = forest[row][column]
  if trees_left == [] or trees_right == [] or trees_above == [] or trees_below == []:
    return 1
  elif height > max(trees_left) or height > max(trees_right) or height > max(trees_above) or height > max(trees_below):
    return 1
  else:
    return 0

input_file = open('input.txt', 'r')
trees = [[int(height) for height in list(row)] for row in input_file.read().rstrip().split('\n')]
# print(trees)
is_visible = [[is_visible(row, column, trees) for column in range(len(trees[row]))] for row in range(len(trees))]
# print(is_visible)
no_visible = sum([sum(row) for row in is_visible])
print(no_visible)