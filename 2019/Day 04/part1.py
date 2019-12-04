in_f = open("input.txt", "r")
contents = in_f.read()

min_val = int(contents.split("-")[0])
max_val = int(contents.split("-")[1])

possible_combos = []
for val in range(min_val, max_val + 1):
    if len(str(val)) != 6:
        # print("Not right length - " + str(val))
        continue

    prev_ch = 0
    double_exists = False
    is_decreasing = False
    for ch in str(val):
        if int(ch) < prev_ch:
            is_decreasing = True
        if int(ch) == prev_ch:
            double_exists = True
        prev_ch = int(ch)

    if is_decreasing:
        # print("Decreasing - " + str(val))
        continue
    if not double_exists:
        # print("No double - " + str(val))
        continue

    possible_combos.append(val)

print(possible_combos)
print(len(possible_combos))