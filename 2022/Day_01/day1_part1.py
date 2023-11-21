input_file = open('input.txt', 'r')
calories_sums = [sum([int(calorie) for calorie in calories.split('\n')]) for calories in input_file.read().strip().split('\n\n')]
max_calories = max(calories_sums)
print(f"The highest calorie count is '{max_calories}' from elf number {calories_sums.index(max_calories)}")