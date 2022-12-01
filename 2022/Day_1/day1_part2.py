input_file = open('input.txt', 'r')
calories_sums = [sum([int(calorie) for calorie in calories.split('\n')]) for calories in input_file.read().strip().split('\n\n')]
sorted_calories = sorted(calories_sums, reverse=True)
top_three = sorted_calories[0:3]
print(f"The top three elves have a total of {sum(top_three)} calories between them.")