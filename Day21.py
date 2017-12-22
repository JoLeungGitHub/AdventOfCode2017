'''


input: 


'''
def P1():
	filearray = []
	file = open("Day21input.txt", "r")
	for line in file:
		filearray.append(line.strip("\n"))

	rules = {}
	for rule in filearray:
		before = rule[:rule.find("=>")-1].split("/")
		after = rule[rule.find("=>")+3:].split("/")
		rules[tuple(before)] = after

		b_mirror_y = []
		for l in before:
			b_mirror_y.append(l[::-1])
		rules[tuple(b_mirror_y)] = after

		


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
	return rules

'''


input: 


'''
def P2():
	
	return 

if __name__ == '__main__':
    #print(P1())
    print(P2())