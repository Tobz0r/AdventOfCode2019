
def read_input(filename):
    with open(filename) as f:
        codes = f.read().strip().split(',')
    data = [index.zfill(5) for index in codes]
    return data


def part_1(data, noun=12,verb=2):
    index = 0
    while(True):
        operation = int(data[index][-2] + data[index][-1])
        mode_1 = int(data[index][-3])
        mode_2 = int(data[index][-4])
        noun = int(data[index + 1])
        verb = int(data[index + 2])
        if operation == 1:
            if mode_1 == 0:
                noun = data[int(data[index + 1])]
            if mode_2 == 0:
                verb = data[int(data[index + 2])]
            data[int(data[index+3])] = str(int(noun) + int(verb))
            index += 4
        elif operation == 2:
            if mode_1 == 0:
                noun = data[int(data[index + 1])]
            if mode_2 == 0:
                verb = data[int(data[index + 2])]
            data[int(data[index+3])] = str(int(noun) * int(verb))
            index += 4
        elif operation == 99:
            break
        elif operation == 3:
            data[int(data[index+1])] = input()
            index += 2
        elif operation == 4:
            if mode_1 == 0:
                noun = data[noun]
            print(noun)
            index += 2
        elif operation == 5:
            if mode_1 == 0:
                noun = data[int(data[index + 1])]
            if mode_2 == 0:
                verb = data[int(data[index + 2])]
            if int(noun) != 0:
                index = int(verb)
            else:
                index += 3
        elif operation == 6:
            if mode_1 == 0:
                noun = data[int(data[index + 1])]
            if mode_2 == 0:
                verb = data[int(data[index + 2])]
            if int(noun) == 0:
                index = int(verb)
            else:
                index += 3
        elif operation == 7:
            if mode_1 == 0:
                noun = data[int(data[index + 1])]
            if mode_2 == 0:
                verb = data[int(data[index + 2])]
            if int(noun) < int(verb):
                data[int(data[index + 3])] = str(1).zfill(5)
            else:
                data[int(data[index + 3])] = str(0).zfill(5)

            index += 4
        elif operation == 8:
            if mode_1 == 0:
                noun = data[int(data[index + 1])]
            if mode_2 == 0:
                verb = data[int(data[index + 2])]
            if int(noun) == int(verb):
                data[int(data[index + 3])] = str(1).zfill(5)
            else:
                data[int(data[index + 3])] = str(0).zfill(5)

            index += 4
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

