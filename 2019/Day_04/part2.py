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
    doubles = {}
    is_decreasing = False
    for ch in str(val):
        if int(ch) < prev_ch:
            is_decreasing = True
        if int(ch) == prev_ch:
            if int(ch) in doubles:
                doubles[int(ch)] = (True, True)
            else:
                doubles[int(ch)] = (True, False)

        prev_ch = int(ch)

    if is_decreasing:
        # print("Decreasing - " + str(val))
        continue

    pair_exists = False
    for vals in doubles.values():
        if not vals[1]:
            pair_exists = True

    if not pair_exists:
        # print("No pair - " + str(val))
        continue

    possible_combos.append(val)

print(possible_combos)
print(len(possible_combos))