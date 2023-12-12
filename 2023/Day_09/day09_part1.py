file_name = "input.txt"

def continue_sequence(sequence: list) -> list:
  new_sequence = sequence.copy()
  if all([num == 0 for num in sequence]):
    new_sequence.append(0)
    return new_sequence
  
  differences = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
  differences_continued = continue_sequence(differences)
  new_sequence.append(new_sequence[-1] + differences_continued[-1])

  return new_sequence

input_file = open(file_name, 'r')
sequences = [[int(num) for num in line.split(" ")] for line in input_file.read().rstrip().split('\n')]
continued_sequences = [continue_sequence(sequence) for sequence in sequences]

print(f"The sum of all next steps in each sequence is {sum([sequence[-1] for sequence in continued_sequences])}")