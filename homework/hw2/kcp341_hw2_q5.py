
def split_parity(lst):
	pointer = 0
	for i in range(len(lst)):
		if lst[i]%2==1:
			lst[pointer],lst[i] = lst[i],lst[pointer]
			pointer+=1
	return lst











