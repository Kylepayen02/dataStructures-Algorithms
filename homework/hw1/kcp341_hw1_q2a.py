#2a
def shift(lst,k):
	for i in range(k):
		lst.append(lst.pop(0))
	return lst

