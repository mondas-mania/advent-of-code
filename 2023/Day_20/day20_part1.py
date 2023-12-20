file_name = "input_test.txt"
start = "broadcaster"


input_file = open(file_name, 'r')
configuration = {line.split(" -> ")[0]: line.split(" -> ")[1].split(",") for line in input_file.read().rstrip().split('\n')}

None