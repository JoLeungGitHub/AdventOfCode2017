'''
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw).

input: Day11input.txt

Your puzzle answer was 818.
'''
def hexEdP1():
	file = open("Day11input.txt", "r")
	for line in file:
		filearray = line.strip("\n")
	moves = filearray.split(",")

	x = 0
	y = 0
	for move in moves:
		if move == "nw":
			x -= 1
			y += 1
		elif move == "n":
			y += 1			
		elif move == "ne":
			x += 1
			y += 1
		elif move == "sw":
			x -= 1
			y -= 1
		elif move == "s":
			y -= 1
		else: #se
			x += 1
			y -= 1
	return abs(x) + abs(y) - min(abs(x), abs(y))

'''
--- Part Two ---

How many steps away is the furthest he ever got from his starting position?

input: Day11input.txt

Your puzzle answer was 1596.
'''
def hexEdP2():
	file = open("Day11input.txt", "r")
	for line in file:
		filearray = line.strip("\n")
	moves = filearray.split(",")

	x = 0
	y = 0
	furthest = 0
	for move in moves:
		if move == "nw":
			x -= 1
			y += 1
		elif move == "n":
			y += 1			
		elif move == "ne":
			x += 1
			y += 1
		elif move == "sw":
			x -= 1
			y -= 1
		elif move == "s":
			y -= 1
		else: #se
			x += 1
			y -= 1
		current = abs(x) + abs(y) - min(abs(x), abs(y))
		if current > furthest:
			furthest = current
	return furthest

if __name__ == '__main__':
    print(hexEdP1())
    print(hexEdP2())