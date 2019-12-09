import re

START = 146810
FINISH = 612564

def check_input(num):
    """docstring"""
    double = False
    for i in range(5):
        if num[i] > num[i+1]:
            return False
        if num[i] == num[i+1]:
            double = True
    return double

def check_doubles(num):
    for x in str(num):
        if str(num).count(x)==2:
            return True
    return False

def incs(num):
    return min([1 if int(x)<=int(str(num)[e+1]) else 0 for e,x in enumerate(str(num)[:-1])])==1

part1list = [num for num in range(START, FINISH+1) if check_input(([int(x) for x in str(num)]))]
part2list = [num for num in range(START, FINISH+1) if check_doubles(num) and incs(num)]
print(len(part1list))
print(len(part2list))


