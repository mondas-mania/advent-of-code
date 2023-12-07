file_name = "input.txt"

def get_calibration_value(line: str) -> int:
  digits = "".join(filter(str.isdigit, line))
  calibration_value = str(digits[0]) + str(digits[-1])
  return calibration_value

input_file = open(file_name, 'r')
lines = [line for line in input_file.read().rstrip().split('\n')]
calibration_values = [int(get_calibration_value(line)) for line in lines]
print(f"The sum of calibration values is {sum(calibration_values)}.")
