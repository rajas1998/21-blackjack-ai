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

soft = [[0.0 for i in range(6)] for i in range(22)]
soft[21][4] = 1
soft[20][3] = 1
soft[19][2] = 1
soft[18][1] = 1
soft[17][0] = 1
for i in range(16,10,-1):
	for j in range(6):
		for k in range(1,10):
			if (k + i <= 21):
				soft[i][j] += complement_p * soft[i+k][j]
			else:
				soft[i][j] += complement_p * hard[i+k-10][j]
		soft[i][j] += p * hard[i+k-10][j]
for i in range(5,1,-1):
	for j in range(6):
		for k in range(2,10):
			hard[i][j] += complement_p * hard[k+i][j]
		hard[i][j] += p * hard[10+i][j]
		hard[i][j] += complement_p * soft[11+i][j]

print "The value of complement is ", complement_p
for i in hard:
	print i," - ",sum(i)
print "Soft ---------------------------"
for i in soft:
	print i," - ",sum(i)

payoff = [[0.0 for i in range(22)] for i in range(12)]
for i in range(2,11):
	for j in range(22):
		for k in range(5):
			if (17 + k > j):
				payoff[i][j] += hard[i][k] * (-1)
			elif (17 + k < j):
				payoff[i][j] += hard[i][k] * (1)
		payoff[i][j] += hard[i][5] * 1
for j in range(22):
	for k in range(5):
		if (17 + k > j):
			payoff[11][j] += soft[11][k] * (-1)
		elif (17 + k < j):
			payoff[11][j] += soft[11][k] * (1)
	payoff[11][j] += hard[11][5] * 1
payoff[11][21] += p * (-1)
payoff[10][21] += complement_p * (-1)
print
print
for i in range(len(payoff)):
	print i," ..... ", payoff[i]
	print
	print