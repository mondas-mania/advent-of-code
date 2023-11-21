input_file = open('input.txt', 'r')
pairs = [[[*range(int(sectors.split('-')[0]), int(sectors.split('-')[1]) + 1)] for sectors in pair.split(',')] for pair in input_file.read().strip().split('\n')]
common_items = [set(pair[0]).intersection(set(pair[1])) for pair in pairs]
any_overlap = [1 if len(overlap) > 0 else 0 for overlap in common_items]
print(f"The number of pairs with any overlap is: {sum(any_overlap)}")