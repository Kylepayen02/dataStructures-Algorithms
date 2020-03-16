def e_approx(n):
	count=1
	sum=0
	for i in range(1,n+1):
		sum += 1/(count)
		count*=i
	return sum



