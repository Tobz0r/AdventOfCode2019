import math

def read_input(filename):
	with open('input.txt','r') as input:
		input_str = input.read().split('\n')
	data = [int(i) for i in input_str]
	print("hej")
	return data

def part_1(data):
	sum = 0
	for mass in data:
		mass=math.floor(mass/3)
		mass-=2
		sum+=mass
	return sum

def part_2(data):
	sum = 0
	for mass in data:
		i = 0
		while (True):
			mass=math.floor(mass/3)
			mass-=2
			if mass < 0:
				sum += i
				break
			i+=mass
	return sum

			
print(part_1(read_input("input.txt")))
print(part_2(read_input("input.txt")))


