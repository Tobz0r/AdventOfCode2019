
def read_input(filename):
	with open(filename) as f:
		codes = f.read().strip().split(',')
	data = [int(i) for i in codes]
	return data


def part_1(prog, noun=12,verb=2):
	index = 0
	data = prog[:]
	data[1] = noun
	data[2] = verb
	while(True):
		if data[index] == 1:
			data[data[index+3]] = data[data[index+1]] + data[data[index+2]]
		elif data[index] == 2:
			data[data[index+3]] = data[data[index+1]] * data[data[index+2]]
		elif data[index] == 99:
			break
		else:
			print("SOMETHINGS WRONG")
		index+=4
	return data[0]


def part_2():
	for noun in range(100):
		for verb in range(100):
			if part_1(read_input("input.txt"),noun,verb) == 19690720:
				return 100*noun+verb

print(part_1(read_input("input.txt")))
print(part_2())

