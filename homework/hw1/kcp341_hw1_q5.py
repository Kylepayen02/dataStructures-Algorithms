def fibs(n):
	j = 0
	k = 1
	count = 0
	x = True
	while x:
		j, k = k,(j+k) 
		count += 1
		yield j
		if count==n:
			x = False 


