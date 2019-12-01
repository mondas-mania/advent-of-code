import pandas as pd

modules = pd.read_csv('./input.txt', header=None)[0]
fuel_costs = []
current_fuel = 0
for module in modules:
	current_fuel = module // 3
	current_fuel = current_fuel - 2
	# print(current_fuel)
	fuel_costs.append(current_fuel)

print("TOTAL = " + str(sum(fuel_costs)))