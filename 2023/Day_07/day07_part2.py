from collections import Counter

file_name = "input.txt"

card_values = {
  "J": 2,
  "2": 3,
  "3": 4,
  "4": 5,
  "5": 6,
  "6": 7,
  "7": 8,
  "8": 9,
  "9": 10,
  "T": 11,
  "Q": 12,
  "K": 13,
  "A": 14
}

strength_values = {
  6: "Five of a kind",
  5: "Four of a kind",
  4: "Full house",
  3: "Three of a kind",
  2: "Two pair",
  1: "One pair",
  0: "High card",
}

def get_strength(hand: list) -> int:
  counts = Counter(hand)
  unique_cards = len(counts.keys())
  if unique_cards == 1:
    # five of a kind
    return 6
  elif unique_cards == 2:
    # can only be four of a kind or full house
    if 4 in counts.values():
      # four of a kind
      return 5
    else:
      # full house
      return 4
  elif 3 in counts.values():
    # 3 of a kind but not full house
    return 3
  elif unique_cards == 3:
    # two pair, not 3 of a kind
    return 2
  elif unique_cards == 4:
    # single pair
    return 1
  # if not returned already then high card
  return 0


def replace_joker(hand: list) -> list:
  new_hands = []
  if "J" not in hand or hand.count("J") == 5:
    new_hands.append(hand)
    return new_hands
  
  counts = Counter(hand)
  unique_cards = list(counts.keys())
  unique_cards.remove("J")
  for card in unique_cards:
    hand_copy = hand.copy()
    hand_copy = "".join(hand_copy)
    hand_copy = hand_copy.replace("J", card, 1)
    hand_copy = list(hand_copy)
    new_hands += replace_joker(hand_copy)
  
  return new_hands


def get_hand_value(hand: list) -> int:
  sum = 0
  for i in range(5):
    # ensures an earlier card will always have more weight
    sum += card_values[hand[i]] * 14**(5-i)

  hand_permutations = replace_joker(hand)
  hand_strengths = [get_strength(hand_permutation) for hand_permutation in hand_permutations]
  
  # max value from cards alone is 7,529,536
  # so strength multiplier needs to be arbitrarily more
  # to ensure proper weighting
  sum += 10000000 * max(hand_strengths)
  return sum


input_file = open(file_name, 'r')
original_bets = {pair[0]: int(pair[1]) for pair in [line.split(" ") for line in input_file.read().rstrip().split('\n')]}
hand_values = {hand: get_hand_value(list(hand)) for hand in original_bets.keys()}

sorted_list = sorted([[k, v] for k, v in hand_values.items()], key=lambda x: x[1])
multiplied_bets = {hand[0]: original_bets[hand[0]] * (i + 1) for i, hand in enumerate(sorted_list)}
print(f"The total sum of winnings is {sum(list(multiplied_bets.values()))}")
