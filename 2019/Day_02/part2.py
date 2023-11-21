import pandas as pd

inf = list(pd.read_csv('input.txt', header=None).iloc[0])
# print(input)
# print(len(input))
noun = input("Input your noun: ")
verb = input("Input your verb: ")
inf[1] = int(noun)
inf[2] = int(verb)
i = 0
while i < len(inf):
    try:
        code1 = int(inf[i])
        # print(code1)
        code2 = int(inf[i+1])
        # print(code1, code2)
        code3 = int(inf[i+2])
        # print(code1, code2, code3)
        code4 = int(inf[i+3])
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
            val1 = inf[code2]
            val2 = inf[code3]
            inf[code4] = val1 + val2
            # print("INPUT[" + str(code4) + "] = " + str(val1) + " + " + str(val2))
        elif code1 == 2:
            val1 = inf[code2]
            val2 = inf[code3]
            inf[code4] = val1 * val2
            # print("INPUT[" + str(code4) + "] = " + str(val1) + " * " + str(val2))
        else:
            print("??????")
    except:
        print(i, code1)
        print("whoops that index is too far")
    i += 4

print(inf)

# noun changes first half
# verb changes second half
# 4847 is 19690720


