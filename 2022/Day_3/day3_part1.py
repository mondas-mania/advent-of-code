input_file = open('input.txt', 'r')
rucksacks = [[list(rucksack)[:len(rucksack)//2], list(rucksack)[len(rucksack)//2:]] for rucksack in input_file.read().strip().split('\n')]
common_items = [set(rucksack[0]).intersection(rucksack[1]).pop() for rucksack in rucksacks]
priorities = [ord(item)-96 if item.islower() else ord(item)-38 for item in common_items]
print(f"The sum of priorities is: {sum(priorities)}")