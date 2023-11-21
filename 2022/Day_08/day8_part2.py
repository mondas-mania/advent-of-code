def scenic_score(row: int, column: int, forest: list):
  height = forest[row][column]
  trees_left = [1 if tree < height else 0 for tree in forest[row][:column][::-1]]
  trees_right = [1 if tree < height else 0  for tree in forest[row][column+1:]]
  trees_above = [1 if forest[i][column] < height else 0 for i in range(0,row)][::-1]
  trees_below = [1 if forest[i][column] < height else 0 for i in range(row + 1, len(forest))]
  if trees_left == [] or trees_right == [] or trees_above == [] or trees_below == []:
    return 0

  score_left = len(trees_left) if 0 not in trees_left else trees_left.index(0) + 1
  score_right = len(trees_right) if 0 not in trees_right else trees_right.index(0) + 1
  score_above = len(trees_above) if 0 not in trees_above else trees_above.index(0) + 1
  score_below = len(trees_below) if 0 not in trees_below else trees_below.index(0) + 1

  return score_left * score_right * score_above * score_below

input_file = open('input.txt', 'r')
trees = [[int(height) for height in list(row)] for row in input_file.read().rstrip().split('\n')]
# print(trees)
scenic_scores = [[scenic_score(row, column, trees) for column in range(len(trees[row]))] for row in range(len(trees))]
print(scenic_scores)
high_score = max([max(row) for row in scenic_scores])
print(high_score)