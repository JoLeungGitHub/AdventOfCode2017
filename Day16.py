'''
--- Day 16: Permutation Promenade ---
You come upon a very unusual sight; a group of programs here appear to be dancing.

There are sixteen programs in total, named a through p. They start by standing in a line: a stands in position 0, b stands in position 1, and so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:

Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
Exchange, written xA/B, makes the programs at positions A and B swap places.
Partner, written pA/B, makes the programs named A and B swap places.
For example, with only five programs standing in a line (abcde), they could do the following dance:

s1, a spin of size 1: eabcd.
x3/4, swapping the last two programs: eabdc.
pe/b, swapping programs e and b: baedc.
After finishing their dance, the programs end up in order baedc.

You watch the dance for a while and record their dance moves (your puzzle input). In what order are the programs standing after their dance?

input: Day16input.txt

Your puzzle answer was kbednhopmfcjilag.
'''
def permutationPromenade1():
	moves = []
	file = open("Day16input.txt", "r")
	for line in file:
		moves = line.split(",")

	programs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
	for move in moves:
		if move[0] == "s":
			for i in range(int(move[1:])):
				programs.insert(0, programs.pop())
		elif move[0] == "x":
			programs[int(move[1:move.find("/")])], programs[int(move[move.find("/")+1:])] = programs[int(move[move.find("/")+1:])], programs[int(move[1:move.find("/")])]
		else:
			one = programs.index(move[1:move.find("/")])
			two = programs.index(move[move.find("/")+1:])
			programs[one], programs[two] = programs[two], programs[one]
	return "".join(programs)


def oneCycle(n, m):
	programs = n
	for move in m:
		if move[0] == "s":
			for i in range(int(move[1:])):
				programs.insert(0, programs.pop())
		elif move[0] == "x":
			programs[int(move[1:move.find("/")])], programs[int(move[move.find("/")+1:])] = programs[int(move[move.find("/")+1:])], programs[int(move[1:move.find("/")])]
		elif move[0] == "p":
			one = programs.index(move[1:move.find("/")])
			two = programs.index(move[move.find("/")+1:])
			programs[one], programs[two] = programs[two], programs[one]
	return programs

'''
--- Part Two ---
Now that you're starting to get a feel for the dance moves, you turn your attention to the dance as a whole.

Keeping the positions they ended up in from their previous dance, the programs perform it again and again: including the first dance, a total of one billion (1000000000) times.

In the example above, their second dance would begin with the order baedc, and use the same dance moves:

s1, a spin of size 1: cbaed.
x3/4, swapping the last two programs: cbade.
pe/b, swapping programs e and b: ceadb.
In what order are the programs standing after their billion dances?

input: Day16input.txt

Your puzzle answer was fbmcgdnjakpioelh.
'''
def permutationPromenadeP2():
	moves = []
	file = open("Day16input.txt", "r")
	for line in file:
		moves = line.split(",")

	programs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
	cycles = []
	for zzz in range(1000000000):
		oneCycle(programs, moves)
		if programs in cycles:
			return "".join(cycles[(1000000000 % len(cycles))-1])
		cycles.append(programs[:])
	return "".join(programs)

if __name__ == '__main__':
    print(permutationPromenadeP1())
    print(permutationPromenadeP2())