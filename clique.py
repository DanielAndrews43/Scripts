def clique(n):
	total = 0
	print "in a clique"
	total += 1
	for j in range(n):
		total += 1
		for i in range(j):
			total += 1
			print i, "is friends with", j
			total += 1
	print total

clique(4)