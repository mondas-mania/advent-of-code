file_name = "input.txt"

def card_copy_wins(card_copies: dict, card_number: int) -> int:
  copies =  card_copies[card_number]
  total = 1
  if copies == []:
    return total
  
  for copy in copies:
    total += card_copy_wins(card_copies, copy)

  return total

input_file = open(file_name, 'r')
lines = [line for line in input_file.read().rstrip().split('\n')]
cards = {int(line.split(":")[0][5:].strip()): [[value.strip() for value in values.strip().split(" ")] for values in line.split(":")[1].strip().replace("  ", " ").split(" | ")] for line in lines}

card_wins = {card_number: sum([1 if number in card_values[0] else 0 for number in card_values[1]]) for card_number, card_values in cards.items()}
card_copies = {card_number: [int(card_number) + 1 + copy_number for copy_number in range(wins)] for card_number, wins in card_wins.items()}
card_copies_transitive = {card_number: card_copy_wins(card_copies, card_number) for card_number, copies in card_copies.items()}

print(f"The sum of wins is {sum(list(card_copies_transitive.values()))}.")
