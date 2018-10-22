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
		soft[i][j] += p * hard[i][j]
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

standPayoff = [[0.0 for i in range(22)] for i in range(12)]
for i in range(2,11):
	for j in range(22):
		for k in range(5):
			if (17 + k > j):
				standPayoff[i][j] += hard[i][k] * (-1)
			elif (17 + k < j):
				standPayoff[i][j] += hard[i][k] * (1)
		standPayoff[i][j] += hard[i][5] * 1
for j in range(22):
	for k in range(5):
		if (17 + k > j):
			standPayoff[11][j] += soft[11][k] * (-1)
		elif (17 + k < j):
			standPayoff[11][j] += soft[11][k] * (1)
	standPayoff[11][j] += hard[11][5] * 1
standPayoff[11][21] += p * (-1)
standPayoff[10][21] += complement_p * (-1)
print
print
for i in range(len(standPayoff)):
	print i," ..... ", standPayoff[i]
	print
	print


###########################################

bestHardPayoff = [[0.0 for i in range(22)] for i in range(12)]
bestHardMove = [["" for i in range(22)] for i in range(12)]
for i in range(12):
	bestHardPayoff[i][21] = standPayoff[i][21]

for i in range(2,12,1):
	for j in range(21,10,-1):
		hitPayoff = 0.0
		doublePayoff = 0.0
		for k in range(1,10,1):
			if (k + j <= 21):
				hitPayoff += complement_p * bestHardPayoff[i][k+j]
				doublePayoff += 2 * complement_p * standPayoff[i][k+j]
			else:
				hitPayoff += complement_p * (-1)
				doublePayoff += 2 * complement_p * (-1)
		if (10 + j <= 21):
			hitPayoff += p * bestHardPayoff[i][10+j]
			doublePayoff += 2 * p * standPayoff[i][10+j]
		else:
			hitPayoff += p * (-1)
			doublePayoff += 2 * p * (-1)

		bestHardPayoff[i][j] = max(hitPayoff,standPayoff[i][j],doublePayoff)
		if(bestHardPayoff[i][j] == hitPayoff):
			bestHardMove[i][j] = "H"
		elif(bestHardPayoff[i][j] == standPayoff[i][j]):
			bestHardMove[i][j] = "S"
		else:
			bestHardMove[i][j] = "D"

print
print
# print bestHardMove
for i in range(22):
	for j in range(2,12):
		print bestHardMove[j][i],
	print

bestSoftPayoff = [[0.0 for i in range(22)] for i in range(12)]
bestSoftMove = [["" for i in range(22)] for i in range(12)]
for i in range(12):
	bestSoftPayoff[i][21] = standPayoff[i][21]

for i in range(2,12,1):
	for j in range(20,12,-1):
		hitPayoff = 0.0
		doublePayoff = 0.0
		for k in range(1,10,1):
			if (k + j <= 21):
				hitPayoff += complement_p * bestSoftPayoff[i][k+j]
				doublePayoff += 2 * complement_p * standPayoff[i][k+j]
			else:
				hitPayoff += complement_p * bestHardPayoff[i][k+j-10]
				doublePayoff += 2 * complement_p * standPayoff[i][k+j-10]
		# if (10 + j <= 21):
		# 	hitPayoff += p * bestSoftPayoff[i][10+j]
		# 	doublePayoff += 2 * p * standPayoff[i][10+j]

		hitPayoff += p * bestHardPayoff[i][j]
		doublePayoff += 2 * p * standPayoff[i][j]

		bestSoftPayoff[i][j] = max(hitPayoff,standPayoff[i][j],doublePayoff)
		if(bestSoftPayoff[i][j] == hitPayoff):
			bestSoftMove[i][j] = "H"
		elif(bestSoftPayoff[i][j] == standPayoff[i][j]):
			bestSoftMove[i][j] = "S"
		else:
			bestSoftMove[i][j] = "D"

print
print
# print bestHardMove
for i in range(22):
	for j in range(2,12):
		print bestSoftMove[j][i],
	print
###########################################
