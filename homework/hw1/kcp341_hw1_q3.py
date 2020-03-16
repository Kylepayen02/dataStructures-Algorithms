#a
def func1(n):
	count = 0
	lst = [i**2 for i in range(1,n)]
	for i in lst: 
		count+=i
	return count

#b
x = sum([i**2 for i in range(1,n)])

#c
def func3(n):
	count = 0
	lst = [i**2 for i in range(1,n) if i%2!=0]
	for i in lst: 
		count+=i
	return count


#d
y = sum([i**2for i in range(1,n) if i%2!=0])

