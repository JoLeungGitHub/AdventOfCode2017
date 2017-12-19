'''
--- Day 19: A Series of Tubes ---
Somehow, a network packet got lost and ended up here. It's trying to follow a routing diagram (your puzzle input), but it's confused about where to go.

Its starting point is just off the top of the diagram. Lines (drawn with |, -, and +) show the path it needs to take, starting by going down onto the only line connected to the top of the diagram. It needs to follow this path until it reaches the end (located somewhere within the diagram) and stop there.

Sometimes, the lines cross over each other; in these cases, it needs to continue going the same direction, and only turn left or right when there's no other option. In addition, someone has left letters on the line; these also don't change its direction, but it can use them to keep track of where it's been. For example:

     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 

Given this diagram, the packet needs to take the following path:

Starting at the only line touching the top of the diagram, it must go down, pass through A, and continue onward to the first +.
Travel right, up, and right, passing through B in the process.
Continue down (collecting C), right, and up (collecting D).
Finally, go all the way left through E and stopping at F.
Following the path to the end, the letters it sees on its path are ABCDEF.

The little packet looks up at you, hoping you can help it find the way. What letters will it see (in the order it would see them) if it follows the path? (The routing diagram is very wide; make sure you view it without line wrapping.)

input: Day19input.txt

Your puzzle answer was DTOUFARJQ.
'''
def P1():
	maze = []
	file = open("Day19input.txt", "r")
	for line in file:
		maze.append(line.strip("\n"))
	x = 75
	y = 0
	word = ""
	flow = "d"
	while x != 0 or y != 199:
		if maze[y][x] != "+":
			if maze[y][x] != "-" and maze[y][x] != "|":
				word = word + maze[y][x]
			if flow == "d":
				y += 1
			elif flow == "u":
				y -= 1
			elif flow == "r":
				x += 1
			elif flow == "l":
				x -= 1
		else:
			if flow == "d" or flow == "u":
				if maze[y][x+1] == "-":
					flow = "r"
					x += 1
				else:
					flow = "l"
					x -= 1
			else:
				if maze [y+1][x] == "|":
					flow = "d"
					y += 1
				else:
					flow = "u"
					y -= 1
	return word

'''
--- Part Two ---
The packet is curious how many steps it needs to go.

For example, using the same routing diagram from the example above...

     |          
     |  +--+    
     A  |  C    
 F---|--|-E---+ 
     |  |  |  D 
     +B-+  +--+ 

...the packet would go:

6 steps down (including the first line at the top of the diagram).
3 steps right.
4 steps up.
3 steps right.
4 steps down.
3 steps right.
2 steps up.
13 steps left (including the F it stops on).
This would result in a total of 38 steps.

How many steps does the packet need to go?

input: Day19input.txt

Your puzzle answer was 16642.
'''
def P2():
	maze = []
	file = open("Day19input.txt", "r")
	for line in file:
		maze.append(line.strip("\n"))
	x = 75
	y = 0
	steps = 0
	flow = "d"
	while x != 0 or y != 199:
		if maze[y][x] != "+":
			if flow == "d":
				steps += 1
				y += 1
			elif flow == "u":
				steps += 1
				y -= 1
			elif flow == "r":
				steps += 1
				x += 1
			elif flow == "l":
				steps += 1
				x -= 1
		else:
			if flow == "d" or flow == "u":
				if maze[y][x+1] == "-":
					steps += 1
					flow = "r"
					x += 1
				else:
					steps += 1
					flow = "l"
					x -= 1
			else:
				if maze [y+1][x] == "|":
					steps += 1
					flow = "d"
					y += 1
				else:
					steps += 1
					flow = "u"
					y -= 1
	return steps

if __name__ == '__main__':
    print(P1())
    print(P2())