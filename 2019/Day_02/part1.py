import pandas as pd

input = list(pd.read_csv('input.txt', header=None).iloc[0])
# print(input)
# print(len(input))
i = 0
while i < len(input):
    try:
        code1 = int(input[i])
        # print(code1)
        code2 = int(input[i+1])
        # print(code1, code2)
        code3 = int(input[i+2])
        # print(code1, code2, code3)
        code4 = int(input[i+3])
        # print(code1, code2, code3, code4)
    except:
        print("position doesn't exist")
        break

    # print("OPCODE " + str(code1))
    if code1 == 99 or code1 not in [1, 2]:
        print("BREAKING")
        break

    try:
        if code1 == 1:
            val1 = input[code2]
            val2 = input[code3]
            input[code4] = val1 + val2
            # print("INPUT[" + str(code4) + "] = " + str(val1) + " + " + str(val2))
        elif code1 == 2:
            val1 = input[code2]
            val2 = input[code3]
            input[code4] = val1 * val2
            # print("INPUT[" + str(code4) + "] = " + str(val1) + " * " + str(val2))
        else:
            print("??????")
    except:
        print("whoops that index is too far")
    i += 4

print(input)


