'''
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?

input: Day8input.txt

Your puzzle answer was 3089.
'''
def likeRegistersP1():
	filearray = []
	file = open("Day8input.txt", "r")
	for line in file:
		filearray.append(line.strip("\n"))
	
	registers = {}
	for line in filearray:
		name = line[:line.find(" ")]
		registers[name] = 0

	for line in filearray:
		name = line[:line.find(" ")]
		if isCondition(registers, line[line.find("if")+3:]):
			if line[line.find(" ")+1:line.find(" ")+4] == "dec":
				registers[name] -= int(line[line.find(" ")+5:line.find("if")-1])
			else:
				registers[name] += int(line[line.find(" ")+5:line.find("if")-1])
	largest = max(registers, key=registers.get)
	return registers[largest]

'''
--- Part Two ---

To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).

input: Day8input.txt

Your puzzle answer was 5391.
'''
def likeRegistersP2():
	filearray = []
	file = open("Day8input.txt", "r")
	for line in file:
		filearray.append(line.strip("\n"))
	
	registers = {}
	for line in filearray:
		name = line[:line.find(" ")]
		registers[name] = 0

	largest = 0
	for line in filearray:
		name = line[:line.find(" ")]
		if isCondition(registers, line[line.find("if")+3:]):
			if line[line.find(" ")+1:line.find(" ")+4] == "dec":
				registers[name] -= int(line[line.find(" ")+5:line.find("if")-1])
			else:
				registers[name] += int(line[line.find(" ")+5:line.find("if")-1])
				if registers[name] > largest:
					largest = registers[name]
	return largest

#-------------------------------------------------------------------#

def isCondition(registers, condition):
	name = condition[:condition.find(" ")]
	op = condition[condition.find(" ")+1:condition.find(" ", condition.find(" ")+1)]
	num = int(condition[condition.find(" ", condition.find(" ")+1)+1:])

	if op == ">":
		return registers[name] > num
	elif op == "<":
		return registers[name] < num
	elif op == "==":
		return registers[name] == num
	elif op == "!=":
		return registers[name] != num
	elif op == "<=":
		return registers[name] <= num
	else:
		return registers[name] >= num

if __name__ == '__main__':
    print(likeRegistersP1())
    print(likeRegistersP2())