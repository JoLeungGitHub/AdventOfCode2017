'''


input: 


'''
def P1():
	filearray = []
	file = open("Day18input.txt", "r")
	for line in file:
		filearray.append(line.strip("\n"))

	duet = {}
	index = 0
	sound = 0
	while index < len(filearray):
		if filearray[index][4] not in duet:
			duet[filearray[index][4]] = 0
		if filearray[index][:3] == "set":
			if filearray[index][6:] in duet:
				duet[filearray[index][4]] = duet[filearray[index][6:]]
			else:
				duet[filearray[index][4]] = int(filearray[index][6:])
		elif filearray[index][:3] == "add":
			if filearray[index][6:] in duet:
				duet[filearray[index][4]] = duet[filearray[index][4]] + duet[filearray[index][6:]]
			else:
				duet[filearray[index][4]] = duet[filearray[index][4]] + int(filearray[index][6:])
		elif filearray[index][:3] == "mul":
			if filearray[index][6:] in duet:
				duet[filearray[index][4]] = duet[filearray[index][4]] * duet[filearray[index][6:]]
			else:
				duet[filearray[index][4]] = duet[filearray[index][4]] * int(filearray[index][6:])
		elif filearray[index][:3] == "mod":
			if filearray[index][6:] in duet:
				duet[filearray[index][4]] = duet[filearray[index][4]] % duet[filearray[index][6:]]
			else:
				duet[filearray[index][4]] = duet[filearray[index][4]] % int(filearray[index][6:])
		elif filearray[index][:3] == "snd":
			sound = duet[filearray[index][4]]
		elif filearray[index][:3] == "jgz":
			if duet[filearray[index][4]] > 0:
				index = index + int(filearray[index][6:])
				continue;
		elif filearray[index][:3] == "rcv":
			if duet[filearray[index][4]] != 0:
				if sound != 0:
					return sound
		index += 1

'''


input: 


'''
def P2():
	filearray = []
	file = open("Day18input.txt", "r")
	for line in file:
		filearray.append(line.strip("\n"))

	sent = 0

	pZero = {'p': 0, '1': 1}
	indexZero = 0
	sentZero = []
	pZeroWaiting = False
	pOne = {'p': 1, '1': 1}
	indexOne = 0
	sentOne = []
	pOneWaiting = False
	while not (pZeroWaiting and pOneWaiting):
		if not pZeroWaiting:
			if indexZero > 40 or indexZero < 0:
				pZeroWaiting = True
				continue;
			if filearray[indexZero][4] not in pZero:
				pZero[filearray[indexZero][4]] = 0
			if filearray[indexZero][:3] == "set":
				if filearray[indexZero][6:] in pZero:
					pZero[filearray[indexZero][4]] = pZero[filearray[indexZero][6:]]
				else:
					pZero[filearray[indexZero][4]] = int(filearray[indexZero][6:])
			elif filearray[indexZero][:3] == "add":
				if filearray[indexZero][6:] in pZero:
					pZero[filearray[indexZero][4]] = pZero[filearray[indexZero][4]] + pZero[filearray[indexZero][6:]]
				else:
					pZero[filearray[indexZero][4]] = pZero[filearray[indexZero][4]] + int(filearray[indexZero][6:])
			elif filearray[indexZero][:3] == "mul":
				if filearray[indexZero][6:] in pZero:
					pZero[filearray[indexZero][4]] = pZero[filearray[indexZero][4]] * pZero[filearray[indexZero][6:]]
				else:
					pZero[filearray[indexZero][4]] = pZero[filearray[indexZero][4]] * int(filearray[indexZero][6:])
			elif filearray[indexZero][:3] == "mod":
				if filearray[indexZero][6:] in pZero:
					pZero[filearray[indexZero][4]] = pZero[filearray[indexZero][4]] % pZero[filearray[indexZero][6:]]
				else:
					pZero[filearray[indexZero][4]] = pZero[filearray[indexZero][4]] % int(filearray[indexZero][6:])
			elif filearray[indexZero][:3] == "snd":
				sentZero.append(pZero[filearray[indexZero][4]])
				pOneWaiting = False
			elif filearray[indexZero][:3] == "jgz":
				if pZero[filearray[indexZero][4]] > 0:
					if filearray[indexZero][6:] in pZero:
						indexZero = indexZero + pZero[filearray[indexZero][6:]]
						continue;
					else:
						indexZero = indexZero + int(filearray[indexZero][6:])
						continue;
			elif filearray[indexZero][:3] == "rcv":
				if len(sentOne) > 0:
					pZero[filearray[indexZero][4]] = sentOne.pop(0)
				elif len(sentOne) == 0:
					pZeroWaiting = True
			indexZero += 1
			
		if not pOneWaiting:
			if indexOne > 40 or indexOne < 0:
				pOneWaiting = True
				continue;
			if filearray[indexOne][4] not in pOne:
				pOne[filearray[indexOne][4]] = 0
			if filearray[indexOne][:3] == "set":
				if filearray[indexOne][6:] in pOne:
					pOne[filearray[indexOne][4]] = pOne[filearray[indexOne][6:]]
				else:
					pOne[filearray[indexOne][4]] = int(filearray[indexOne][6:])
			elif filearray[indexOne][:3] == "add":
				if filearray[indexOne][6:] in pOne:
					pOne[filearray[indexOne][4]] = pOne[filearray[indexOne][4]] + pOne[filearray[indexOne][6:]]
				else:
					pOne[filearray[indexOne][4]] = pOne[filearray[indexOne][4]] + int(filearray[indexOne][6:])
			elif filearray[indexOne][:3] == "mul":
				if filearray[indexOne][6:] in pOne:
					pOne[filearray[indexOne][4]] = pOne[filearray[indexOne][4]] * pOne[filearray[indexOne][6:]]
				else:
					pOne[filearray[indexOne][4]] = pOne[filearray[indexOne][4]] * int(filearray[indexOne][6:])
			elif filearray[indexOne][:3] == "mod":
				if filearray[indexOne][6:] in pOne:
					pOne[filearray[indexOne][4]] = pOne[filearray[indexOne][4]] % pOne[filearray[indexOne][6:]]
				else:
					pOne[filearray[indexOne][4]] = pOne[filearray[indexOne][4]] % int(filearray[indexOne][6:])
			elif filearray[indexOne][:3] == "snd":
				sentOne.append(pOne[filearray[indexOne][4]])
				pZeroWaiting = False
				sent += 1
			elif filearray[indexOne][:3] == "jgz":
				if pOne[filearray[indexOne][4]] > 0:
					if filearray[indexOne][6:] in pOne:
						indexOne = indexOne + pOne[filearray[indexOne][6:]]
						continue;
					else:
						indexOne = indexOne + int(filearray[indexOne][6:])
						continue;
			elif filearray[indexZero][:3] == "rcv":
				if len(sentZero) > 0:
					pOne[filearray[indexOne][4]] = sentZero.pop(0)
				elif len(sentZero) == 0:
					pOneWaiting = True
			indexOne += 1
	return sent

if __name__ == '__main__':
    #print(P1())
    print(P2())