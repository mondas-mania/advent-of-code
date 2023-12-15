file_name = "input.txt"

def get_hash(hash: str) -> int:
  current_value = 0
  for char in list(hash):
    current_value = current_value + ord(char)
    current_value = current_value * 17
    current_value = current_value % 256
  return current_value

input_file = open(file_name, 'r')
init_seq = (input_file.read().rstrip().split('\n')[0]).split(",")

hash_values = [get_hash(seq) for seq in init_seq]
total = sum(hash_values)

print(f"The sum of all the hashes is {total}")
