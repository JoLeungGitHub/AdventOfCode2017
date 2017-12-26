'''
--- Day 21: Fractal Art ---
You find a program trying to generate some art. It uses a strange process that involves repeatedly enhancing the detail of an image through a set of rules.

The image consists of a two-dimensional square grid of pixels that are either on (#) or off (.). The program always begins with this pattern:

.#.
..#
###
Because the pattern is both 3 pixels wide and 3 pixels tall, it is said to have a size of 3.

Then, the program repeats the following process:

If the size is evenly divisible by 2, break the pixels up into 2x2 squares, and convert each 2x2 square into a 3x3 square by following the corresponding enhancement rule.
Otherwise, the size is evenly divisible by 3; break the pixels up into 3x3 squares, and convert each 3x3 square into a 4x4 square by following the corresponding enhancement rule.
Because each square of pixels is replaced by a larger one, the image gains pixels and so its size increases.

The artist's book of enhancement rules is nearby (your puzzle input); however, it seems to be missing rules. The artist explains that sometimes, one must rotate or flip the input pattern to find a match. (Never rotate or flip the output pattern, though.) Each pattern is written concisely: rows are listed as single units, ordered top-down, and separated by slashes. For example, the following rules correspond to the adjacent patterns:

../.#  =  ..
          .#

                .#.
.#./..#/###  =  ..#
                ###

                        #..#
#..#/..../#..#/.##.  =  ....
                        #..#
                        .##.
When searching for a rule to use, rotate and flip the pattern as necessary. For example, all of the following patterns match the same rule:

.#.   .#.   #..   ###
..#   #..   #.#   ..#
###   ###   ##.   .#.
Suppose the book contained the following two rules:

../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
As before, the program begins with this pattern:

.#.
..#
###
The size of the grid (3) is not divisible by 2, but it is divisible by 3. It divides evenly into a single square; the square matches the second rule, which produces:

#..#
....
....
#..#
The size of this enhanced grid (4) is evenly divisible by 2, so that rule is used. It divides evenly into four squares:

#.|.#
..|..
--+--
..|..
#.|.#
Each of these squares matches the same rule (../.# => ##./#../...), three of which require some flipping and rotation to line up with the rule. The output for the rule is the same in all four cases:

##.|##.
#..|#..
...|...
---+---
##.|##.
#..|#..
...|...
Finally, the squares are joined into a new grid:

##.##.
#..#..
......
##.##.
#..#..
......
Thus, after 2 iterations, the grid contains 12 pixels that are on.

How many pixels stay on after 5 iterations?

input: Day21input.txt

Your puzzle answer was 142.
'''
def fractalArtP1():
	filearray = []
	file = open("Day21input.txt", "r")
	for line in file:
		filearray.append(line.strip("\n"))

	rules = {}
	for rule in filearray:
		before = rule[:rule.find("=>")-1].split("/")
		after = rule[rule.find("=>")+3:].split("/")
		
		rules[tuple(before)] = after
		mirror = mirror(before)
		tules[tules(mirror)] = after

		rotated1 = rotate(before)
		rules[tuple(rotated1)] = after
		mirror1 = mirror(rotated1)
		rules[tuple(mirror1)] = after

		rotated2 = rotate(rotated1)
		rules[tuple(rotated2)] = after
		mirror2 = mirror(rotated2)
		rules[tuple(mirror2)] = after

		rotated3 = rotate(rotated2)
		rules[tuple(rotated3)] = after
		mirror3 = mirror(rotated3)
		rules[tuple(mirror3)] = after

	t = ['.#.', '..#', '###']
	for _ in range(5):
		if len(t) % 2 == 0:
			#divisible by 2
			new = []
			while len(t[len(t)-1]) > 0:
				bit = []
				i = 0
				while i < len(t):
					bit.append(t[i][:2])
					t[i] = t[i][2:]
				new.append(bit)
			
			sized = []
			for __ in range (len(new)):
				sized.append([])

			while len(new[-1]) > 0:
				i = 0
				while i < len(new):
					sized[i].append(tuple(new[i][:2]))
					new[i] = new[i][2:]
					i += 1

			ordered = []
			x = 0
			while x < len(sized):
				y = 0
				while y < len(sized):
					ordered.append(sized[y][x])
					y += 1
				x += 1

			new_t = []
			for group in ordered:
				new_t.append(rules[group])

			t = new_t

		elif len(t) % 3 == 0:
			#divisible by 3
			pass

	amount = 0
	for l in t:
		amount += l.count("#")

	return amount



'''
--- Part Two ---
How many pixels stay on after 18 iterations?

input: Day21input.txt

Your puzzle answer was 1879071.
'''
def fractalArtP2():
	
	return 

#-------------------------------------------------------------------#
def rotate(box):
	returned = []
	for y in range(len(box)):
		temp = []
		for x in range(len(box)-1, -1, -1):
			temp.append(box[x][y])
		returned.append("".join(temp))
	return returned

def mirror(box):
	returned = []
	for l in box:
		returned.append(l[::-1])
	return returned

if __name__ == '__main__':
    #print(fractalArtP1()) Part 1 is incomplete
    #print(fractalArtP2()) Part 2 is Part 1, 18 times