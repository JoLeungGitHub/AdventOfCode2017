'''
--- Day 23: Coprocessor Conflagration ---
You decide to head directly to the CPU and fix the printer from there. As you get close, you find an experimental coprocessor doing so much work that the local programs are afraid it will halt and catch fire. This would cause serious issues for the rest of the computer, so you head in and see what you can do.

The code it's running seems to be a variant of the kind you saw recently on that tablet. The general functionality seems very similar, but some of the instructions are different:

set X Y sets register X to the value of Y.
sub X Y decreases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
Only the instructions listed above are used. The eight registers here, named a through h, all start at 0.

The coprocessor is currently set to some kind of debug mode, which allows for testing, but prevents it from doing any meaningful work.

If you run the program (your puzzle input), how many times is the mul instruction invoked?

input: Day23input.txt

Your puzzle answer was 9409.
'''
def coprocessorConflagrationP1():
	filearray = []
	file = open("Day23input.txt", "r")
	for line in file:
		filearray.append(line.strip("\n"))

	duet = {'1': 1}
	index = 0
	amount = 0
	while index < len(filearray) and index > -1:
		if filearray[index][4] not in duet:
			duet[filearray[index][4]] = 0
		if filearray[index][:3] == "set":
			if filearray[index][6:] in duet:
				duet[filearray[index][4]] = duet[filearray[index][6:]]
			else:
				duet[filearray[index][4]] = int(filearray[index][6:])
		elif filearray[index][:3] == "sub":
			if filearray[index][6:] in duet:
				duet[filearray[index][4]] = duet[filearray[index][4]] - duet[filearray[index][6:]]
			else:
				duet[filearray[index][4]] = duet[filearray[index][4]] - int(filearray[index][6:])
		elif filearray[index][:3] == "mul":
			amount += 1
			if filearray[index][6:] in duet:
				duet[filearray[index][4]] = duet[filearray[index][4]] * duet[filearray[index][6:]]
			else:
				duet[filearray[index][4]] = duet[filearray[index][4]] * int(filearray[index][6:])
		elif filearray[index][:3] == "jnz":
			if duet[filearray[index][4]] != 0:
				index = index + int(filearray[index][6:])
				continue;
		index += 1
	return amount

'''
--- Part Two ---
Now, it's time to fix the problem.

The debug mode switch is wired directly to register a. You flip the switch, which makes register a now start at 1 when the program is executed.

Immediately, the coprocessor begins to overheat. Whoever wrote this program obviously didn't choose a very efficient implementation. You'll need to optimize the program if it has any hope of completing before Santa needs that printer working.

The coprocessor's ultimate goal is to determine the final value left in register h once the program completes. Technically, if it had that... it wouldn't even need to run the program.

After setting register a to 1, if the program were to run to completion, what value would be left in register h?

input: Day23input.txt

Your puzzle answer was 913.
'''
def coprocessorConflagrationP2():
	b = 109900
	c = 126900
	h = 0

	while True:
		if not_prime(b):
			h += 1
		if b == c:
			return h;
		b += 17

#-------------------------------------------------------------------#
def not_prime(n):
	i = 2
	while i * i <= n:
		if n % i == 0:
			return True
		i += 1
	return False

if __name__ == '__main__':
    print(coprocessorConflagrationP1())
    print(coprocessorConflagrationP2())