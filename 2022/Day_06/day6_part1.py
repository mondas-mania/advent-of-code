input_file = open('input.txt', 'r')
communication = input_file.read().rstrip()
communication_chars = list(communication)
groupings = [communication_chars[i-4:i] for i in range(4, len(communication_chars)+1)]
all_different = [1 if len(set(grouping)) == len(grouping) else 0 for grouping in groupings]
first_packet_marker = all_different.index(1) + 4
print(f"The first packet marker is after {first_packet_marker} characters with {communication_chars[first_packet_marker-4:first_packet_marker]}")