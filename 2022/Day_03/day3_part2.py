input_file = open('input.txt', 'r')
rucksacks = [rucksack for rucksack in input_file.read().strip().split('\n')]
grouped_rucksacks = [[list(rucksacks[index*3]), list(rucksacks[index*3+1]), list(rucksacks[index*3+2])] for index in range(len(rucksacks)//3)]
common_items = [set(group[0]).intersection(group[1]).intersection(group[2]).pop() for group in grouped_rucksacks]
priorities = [ord(item)-96 if item.islower() else ord(item)-38 for item in common_items]
print(f"The sum of priorities is: {sum(priorities)}")