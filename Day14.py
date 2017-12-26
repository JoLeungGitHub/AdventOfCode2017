'''
--- Day 14: Disk Defragmentation ---

Suddenly, a scheduled job activates the system's disk defragmenter. Were the situation different, you might sit and watch it for a while, but today, you just don't have that kind of time. It's soaking up valuable system resources that are needed elsewhere, and so the only option is to help it finish its task as soon as possible.

The disk in question consists of a 128x128 grid; each square of the grid is either free or used. On this disk, the state of the grid is tracked by the bits in a sequence of knot hashes.

A total of 128 knot hashes are calculated, each corresponding to a single row in the grid; each hash contains 128 bits which correspond to individual grid squares. Each bit of a hash indicates whether that square is free (0) or used (1).

The hash inputs are a key string (your puzzle input), a dash, and a number from 0 to 127 corresponding to the row. For example, if your key string were flqrgnkx, then the first row would be given by the bits of the knot hash of flqrgnkx-0, the second row from the bits of the knot hash of flqrgnkx-1, and so on until the last row, flqrgnkx-127.

The output of a knot hash is traditionally represented by 32 hexadecimal digits; each of these digits correspond to 4 bits, for a total of 4 * 32 = 128 bits. To convert to bits, turn each hexadecimal digit to its equivalent binary value, high-bit first: 0 becomes 0000, 1 becomes 0001, e becomes 1110, f becomes 1111, and so on; a hash that begins with a0c2017... in hexadecimal would begin with 10100000110000100000000101110000... in binary.

Continuing this process, the first 8 rows and columns for key flqrgnkx appear as follows, using # to denote used squares, and . to denote free ones:

##.#.#..-->
.#.#.#.#   
....#.#.   
#.#.##.#   
.##.#...   
##..#..#   
.#...#..   
##.#.##.-->
|      |   
V      V   
In this example, 8108 squares are used across the entire 128x128 grid.

Given your actual key string, how many squares are used?

input: Day14input.txt

Your puzzle answer was 8074.
'''
def diskDefragmentationP1():
	file = open("Day14input.txt", "r")
	for line in file:
		n = line.strip("\n")

	inputs = []
	for i in range(128):
		inputs.append(n+"-"+str(i))

	hashes = []
	for inp in inputs:
		hashes.append(knotHash(inp))

	hexed = []
	for h in hashes:
		hexed.append(bin(int(h, 16))[2:].zfill(128))

	used = 0
	for l in hexed:
		used += l.count("1")
	return used

'''
--- Part Two ---

Now, all the defragmenter needs to know is the number of regions. A region is a group of used squares that are all adjacent, not including diagonals. Every used square is in exactly one region: lone used squares form their own isolated regions, while several adjacent squares all count as a single region.

In the example above, the following nine regions are visible, each marked with a distinct digit:

11.2.3..-->
.1.2.3.4   
....5.6.   
7.8.55.9   
.88.5...   
88..5..8   
.8...8..   
88.8.88.-->
|      |   
V      V   
Of particular interest is the region marked 8; while it does not appear contiguous in this small view, all of the squares marked 8 are connected when considering the whole 128x128 grid. In total, in this example, 1242 regions are present.

How many regions are present given your key string?

input: Day14input.txt

Your puzzle answer was 1212.
'''
def diskDefragmentationP2():
	file = open("Day14input.txt", "r")
	for line in file:
		n = line.strip("\n")

	inputs = []
	for i in range(128):
		inputs.append(n+"-"+str(i))

	hashes = []
	for inp in inputs:
		hashes.append(knotHash(inp))

	hexed = []
	for h in hashes:
		hexed.append(bin(int(h, 16))[2:].zfill(128))

	check = []
	for i in range(128):
		for j in range(128):
			if hexed[i][j] == "1":
				check.append((i, j))
	groups = 0
	while len(check) > 0:
		nextup = [check[0]]
		while len(nextup) > 0:
			current = nextup.pop()
			if current in check:
				check.remove(current)
				(i, j) = current
				nextup.append((i-1, j))
				nextup.append((i+1, j))
				nextup.append((i, j-1))
				nextup.append((i, j+1))
		groups += 1
	return groups

#-------------------------------------------------------------------#
#Function from Day 10 Part 2
def knotHash(n):
	t = [x for x in range(256)]

	asciiInput = []
	for ch in n:
		asciiInput.append(ord(ch))
	asciiInput = asciiInput + [17, 31, 73, 47, 23]

	skip = 0
	index = 0
	sixtyfour = 64
	while sixtyfour > 0:
		for i in asciiInput:
			if index + i >= len(t):
				reversal = t[index:] + t[:i-len(t[index:])]
			else :
				reversal = t[index:index+i]
			reversal.reverse()
			
			ind = 0
			tempreverse = index
			while ind < i:
				t[tempreverse] = reversal[ind]
				ind += 1
				tempreverse += 1
				if tempreverse == len(t):
					tempreverse = 0

			posforward = i + skip
			while posforward > 0:
				index += 1
				if index == len(t):
					index = 0
				posforward -= 1
			skip += 1
		sixtyfour -= 1
	
	retXOR = []
	retIndex = 16
	while retIndex <= 256:
		xor = 0
		for thing in t[retIndex-16:retIndex]:
			xor = xor ^ thing
		retXOR.append(xor)
		retIndex += 16

	returned = ""

	for element in retXOR:
		add = hex(element)[2:]
		if len(add) < 2:
			add = "0" + add
		returned = returned + add

	return returned

if __name__ == '__main__':
    print(diskDefragmentationP1())
    print(diskDefragmentationP2())