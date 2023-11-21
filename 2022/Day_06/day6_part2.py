no_distinct_chars = 14

input_file = open('input.txt', 'r')
communication = input_file.read().rstrip()
communication_chars = list(communication)
groupings = [communication_chars[i-no_distinct_chars:i] for i in range(no_distinct_chars, len(communication_chars)+1)]
all_different = [1 if len(set(grouping)) == len(grouping) else 0 for grouping in groupings]
first_packet_marker = all_different.index(1) + no_distinct_chars
print(f"The first packet marker is after {first_packet_marker} characters with {communication_chars[first_packet_marker-no_distinct_chars:first_packet_marker]}")