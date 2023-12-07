file_name = "input.txt"
digit_map = {
  "": "",
  "zero": "0",
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
}

def get_calibration_value(line: str) -> int:
  calibration_value = str(get_first_calibration_value(line)) + str(get_last_calibration_value(line))
  return calibration_value

def get_first_calibration_value(line: str) -> str:
  new_line = find_first_num(line)
  digits = "".join(filter(str.isdigit, new_line))
  return int(digits[0])

def get_last_calibration_value(line: str) -> str:
  new_line = find_last_num(line)
  digits = "".join(filter(str.isdigit, new_line))
  return int(digits[-1])

def find_first_num(line: str) -> str:
  earliest_num = ""
  for string in digit_map.keys():
    pos = line.find(string)
    if pos != -1 and (pos < line.find(earliest_num) or earliest_num == ""):
      earliest_num = string
  new_line = line.replace(earliest_num, digit_map[earliest_num])
  return new_line

def find_last_num(line: str) -> str:
  last_num = ""
  for string in digit_map.keys():
    pos = line.rfind(string)
    if pos != -1 and (pos > line.rfind(last_num) or last_num == ""):
      last_num = string
  new_line = line.replace(last_num, digit_map[last_num])
  return new_line


input_file = open(file_name, 'r')
lines = [line for line in input_file.read().rstrip().split('\n')]
calibration_values = [int(get_calibration_value(line)) for line in lines]
print(f"The sum of calibration values is {sum(calibration_values)}.")
