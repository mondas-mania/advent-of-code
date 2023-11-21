input_file = open('input.txt', 'r')
pairs = [[[*range(int(sectors.split('-')[0]), int(sectors.split('-')[1]) + 1)] for sectors in pair.split(',')] for pair in input_file.read().strip().split('\n')]
pairs_sizes = [[len(sectors) for sectors in pair] for pair in pairs]
common_items = [set(pair[0]).intersection(set(pair[1])) for pair in pairs]
entire_overlap = [1 if len(common_items[i]) == pairs_sizes[i][0] or len(common_items[i]) == pairs_sizes[i][1] else 0 for i in range(len(pairs))]
print(f"The number of pairs with one range encompassing the other is: {sum(entire_overlap)}")