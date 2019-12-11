
def read_input(filename):
	with open(filename) as f:
		codes = f.read().strip().split(',')
	data = [int(i) for i in codes]
	return data

def part_1(prog, noun=12,verb=2):
	index = 0
	data = prog[:]
	while(True):
		print(data[index])
		if data[index] == 1:
			data[data[index+3]] = data[data[index+1]] + data[data[index+2]]
			index+=4
		elif data[index] == 2:
			data[data[index+3]] = data[data[index+1]] * data[data[index+2]]
			index+=4
		elif data[index] == 99:
			break
		elif data[index] == 3:
			data[index+1] = int(input())
			index+=2
		elif data[index] == 4:
			print(data[data[index]])
			index+=2
		else:
			print("SOMETHINGS WRONG")
			break
		

	return data[0]


def part_2():
	for noun in range(100):
		for verb in range(100):
			if part_1(read_input("input.txt"),noun,verb) == 19690720:
				return 100*noun+verb

print(part_1(read_input("input.txt")))
#print(part_2())

