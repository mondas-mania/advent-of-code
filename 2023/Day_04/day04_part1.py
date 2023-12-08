file_name = "input.txt"

input_file = open(file_name, 'r')
lines = [line for line in input_file.read().rstrip().split('\n')]
cards = {line.split(":")[0][5:].strip(): [[value.strip() for value in values.strip().split(" ")] for values in line.split(":")[1].strip().replace("  ", " ").split(" | ")] for line in lines}
# {
#   'n' : [
#     [winning numbers],
#     [card numbers]
#   ]
# }

card_wins = {card_number: sum([1 if number in card_values[0] else 0 for number in card_values[1]]) for card_number, card_values in cards.items()}
card_points = {card_number: 2 ** (wins - 1) if wins > 0 else 0 for card_number, wins in card_wins.items()}

print(f"The sum of points is {sum(list(card_points.values()))}.")
