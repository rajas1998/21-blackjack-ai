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
# print hard[5]
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
		if (10 + i <= 21):
			soft[i][j] += p * soft[i+10][j]
		else:
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
			# if(j==21 and 17 + k < j):
			# 	standPayoff[i][j] += hard[i][k] * (1.5) #BlackJack
			if (17 + k > j):
				standPayoff[i][j] += hard[i][k] * (-1)
			elif (17 + k < j):
				standPayoff[i][j] += hard[i][k] * (1)
		standPayoff[i][j] += hard[i][5] * 1
for j in range(22):
	for k in range(5):
		# if(j==21 and 17 + k < j):
		# 	standPayoff[i][j] += soft[i][k] * (1.5) #BlackJack
		if (17 + k > j):
			standPayoff[11][j] += soft[11][k] * (-1)
		elif (17 + k < j):
			standPayoff[11][j] += soft[11][k] * (1)
	standPayoff[11][j] += hard[11][5] * 1

standPayoff[11][21] += p * (-1)
standPayoff[10][21] += complement_p * (-1)

print
for i in range(len(standPayoff)):
	print i," ..... ", standPayoff[i]
	print
	print


###########################################

bestHardHitOrStandPayoff = [[0.0 for i in range(22)] for i in range(12)]
hardDoublePayoff = [[0.0 for i in range(22)] for i in range(12)]
hardHitPayoff = [[0.0 for i in range(22)] for i in range(12)]
bestHardPayoff = [[0.0 for i in range(22)] for i in range(12)]
bestHardMove = [["" for i in range(22)] for i in range(12)]
for i in range(12):
	bestHardHitOrStandPayoff[i][21] = standPayoff[i][21]

for i in range(2,12,1):
	for j in range(21,10,-1):
		hitPayoff = 0.0
		doublePayoff = 0.0
		for k in range(1,10,1):
			if (k + j <= 21):
				hitPayoff += complement_p * bestHardHitOrStandPayoff[i][k+j]
				doublePayoff += 2 * complement_p * standPayoff[i][k+j]
			else:
				hitPayoff += complement_p * (-1)
				doublePayoff += 2 * complement_p * (-1)
		if (10 + j <= 21):
			hitPayoff += p * bestHardHitOrStandPayoff[i][10+j]
			doublePayoff += 2 * p * standPayoff[i][10+j]
		else:
			hitPayoff += p * (-1)
			doublePayoff += 2 * p * (-1)

		bestHardHitOrStandPayoff[i][j] = max(hitPayoff,standPayoff[i][j])
		hardDoublePayoff[i][j] = doublePayoff
		hardHitPayoff[i][j] = hitPayoff
		bestHardPayoff[i][j] = max(hardHitPayoff[i][j], standPayoff[i][j], hardDoublePayoff[i][j])
		if (bestHardPayoff[i][j] == hardHitPayoff[i][j]):
			bestHardMove[i][j] = "H"
		elif(bestHardPayoff[i][j] == standPayoff[i][j]):
			bestHardMove[i][j] = "S"
		else:
			bestHardMove[i][j] = "D"

print
print


bestSoftHitOrStandPayoff = [[0.0 for i in range(22)] for i in range(12)]
softHitPayoff = [[0.0 for i in range(22)] for i in range(12)]
softDoublePayoff = [[0.0 for i in range(22)] for i in range(12)]
bestSoftPayoff = [[0.0 for i in range(22)] for i in range(12)]
bestSoftMove = [["" for i in range(22)] for i in range(12)]
for i in range(12):
	bestSoftHitOrStandPayoff[i][21] = standPayoff[i][21]

for i in range(2,12,1):
	for j in range(20,12,-1):
		hitPayoff = 0.0
		doublePayoff = 0.0
		for k in range(1,10,1):
			if (k + j <= 21):
				hitPayoff += complement_p * bestSoftHitOrStandPayoff[i][k+j]
				doublePayoff += 2 * complement_p * standPayoff[i][k+j]
			else:
				hitPayoff += complement_p * bestHardHitOrStandPayoff[i][k+j-10]
				doublePayoff += 2 * complement_p * standPayoff[i][k+j-10]
		# if (10 + j <= 21):
		# 	hitPayoff += p * bestSoftHitOrStandPayoff[i][10+j]
		# 	doublePayoff += 2 * p * standPayoff[i][10+j]

		hitPayoff += p * bestHardHitOrStandPayoff[i][j]
		doublePayoff += 2 * p * standPayoff[i][j]

		bestSoftHitOrStandPayoff[i][j] = max(hitPayoff,standPayoff[i][j])
		softHitPayoff[i][j] = hitPayoff
		softDoublePayoff[i][j] = doublePayoff
		bestSoftPayoff[i][j] = max(softHitPayoff[i][j], standPayoff[i][j], softDoublePayoff[i][j])
		if (bestSoftPayoff[i][j] == softHitPayoff[i][j]):
			bestSoftMove[i][j] = "H"
		elif(bestHardPayoff[i][j] == standPayoff[i][j]):
			bestSoftMove[i][j] = "S"
		else:
			bestSoftMove[i][j] = "D"
		# if(j==14 and i==5):
			# print "Printing the incorrect case"
			# print hitPayoff,standPayoff[i][j],doublePayoff
		# if(j==18 and i==11):
			# print "Printing the incorrect case"
			# print hitPayoff,standPayoff[i][j],doublePayoff

		# if(bestSoftHitOrStandPayoff[i][j] == hitPayoff):
			# bestSoftMove[i][j] = "H"
		# elif(bestSoftHitOrStandPayoff[i][j] == standPayoff[i][j]):
			# bestSoftMove[i][j] = "S"
		# else:
			# bestSoftMove[i][j] = "D"
print
print
# print "bestSoftMove"
# for i in range(13,21):
	# for j in range(2,12):
		# print bestSoftMove[j][i],
	# print

for i in range(2,12,1):
	for j in range(10,4,-1):
		hitPayoff = 0.0
		doublePayoff = 0.0
		for k in range(1,10,1):
			if(k==1):
				if(j + 11 <=21):
					hitPayoff += complement_p * bestSoftHitOrStandPayoff[i][j+11]
					doublePayoff += 2 * complement_p * max(standPayoff[i][k+j], standPayoff[i][11+j])
				else:
					hitPayoff += complement_p * bestHardHitOrStandPayoff[i][j+k]
					doublePayoff += 2 * complement_p * standPayoff[i][k+j]
			elif (k + j <= 21):
				hitPayoff += complement_p * bestHardHitOrStandPayoff[i][k+j]
				doublePayoff += 2 * complement_p * standPayoff[i][k+j]
			else:
				hitPayoff += complement_p * (-1)
				doublePayoff += 2 * complement_p * (-1)
		if (10 + j <= 21):
			hitPayoff += p * bestHardHitOrStandPayoff[i][10+j]
			doublePayoff += 2 * p * standPayoff[i][10+j]
		else:
			hitPayoff += p * (-1)
			doublePayoff += 2 * p * (-1)

		bestHardHitOrStandPayoff[i][j] = max(hitPayoff,standPayoff[i][j])
		hardDoublePayoff[i][j] = doublePayoff
		hardHitPayoff[i][j] = hitPayoff
		bestHardPayoff[i][j] = max(hardHitPayoff[i][j], standPayoff[i][j], hardDoublePayoff[i][j])
		if (bestHardPayoff[i][j] == hardHitPayoff[i][j]):
			bestHardMove[i][j] = "H"
		elif(bestHardPayoff[i][j] == standPayoff[i][j]):
			bestHardMove[i][j] = "S"
		else:
			bestHardMove[i][j] = "D"
		# if(i==3 and j==9):
			# print hitPayoff,standPayoff[i][j],doublePayoff
		# if(bestHardHitOrStandPayoff[i][j] == hitPayoff):
			# bestHardMove[i][j] = "H"
		# elif(bestHardHitOrStandPayoff[i][j] == standPayoff[i][j]):
			# bestHardMove[i][j] = "S"
		# else:
			# bestHardMove[i][j] = "D"

# print "bestHardMove"
# for i in range(5,22):
	# for j in range(2,12):
		# print bestHardMove[j][i],
	# print
###########################################

# split = [[0.0 for i in range(12)] for i in range(12)]
# lone = [[0.0 for i in range(12)] for i in range(12)] #2,3......11->A
#
# for i in range(2,12): #My Pair
# 	for j in range(2,12): #Dealer's Card
# 		split[i][j] = max(bestHardHitOrStandPayoff[j][2*i], 2*lone[i][j])
# 		lone[i][j] = bestHardHitOrStandPayoff[j][i]


print 
for j in range(5,22):
	if (j <= 9):
		print "",j," - ",
	else:
		print j," - ",
	for i in range(2,12):
		print bestHardMove[i][j],
	print
print
print 
print "Soft Payoffs are being printed"
for j in range(13,21):
	if (j <= 9):
		print "",j," - ",
	else:
		print j," - ",
	for i in range(2,12):
		print bestSoftMove[i][j],
	print

