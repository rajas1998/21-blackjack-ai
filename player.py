p = float(raw_input())
complement_p = (1-p)/9
hard = [[0.0 for i in range(6)] for i in range(22)]
hard[21][4] = 1
hard[20][3] = 1
hard[19][2] = 1
hard[18][1] = 1
hard[17][0] = 1
for i in range(16,10,-1):
	for j in range(6):
		for k in range(1,10):
			if (k + i <= 21):
				hard[i][j] += complement_p * hard[k+i][j]
			elif j == 5:
				hard[i][j] += complement_p
		if (10 + i <= 21):
				hard[i][j] += p * hard[10+i][j]
		elif j == 5:
			hard[i][j] += p
for i in range(10,5,-1):
	for j in range(6):
		for k in range(2,10) + [11]:
			if (k + i <= 21):
				hard[i][j] += complement_p * hard[k+i][j]
			elif j == 5:
				hard[i][j] += complement_p
		if (10 + i <= 21):
				hard[i][j] += p * hard[10+i][j]
		elif j == 5:
			hard[i][j] += p
for i in hard:
	print i," - ",sum(i)














