'''


input: Day23input.txt


'''
def P1():
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


input: Day23input.txt


'''
def P2():
	filearray = []
	file = open("Day23input.txt", "r")
	for line in file:
		filearray.append(line.strip("\n"))

	duet = {'1': 1, 'a': 1}
	index = 0
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
			if filearray[index][6:] in duet:
				duet[filearray[index][4]] = duet[filearray[index][4]] * duet[filearray[index][6:]]
			else:
				duet[filearray[index][4]] = duet[filearray[index][4]] * int(filearray[index][6:])
		elif filearray[index][:3] == "jnz":
			if duet[filearray[index][4]] != 0:
				index = index + int(filearray[index][6:])
				continue;
		index += 1
	return duet['h']

if __name__ == '__main__':
    print(P1())
    print(P2())