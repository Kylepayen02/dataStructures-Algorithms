#a

def twos_powers(n):
	for i in range(n):
		x=2**i
		yield(x)
# for i in twos_powers(10):
# 	print(i,end=", ")
# print( )


#b
def reverse_twos_powers(n):
	for i in range(n):
		x=.5**i
		yield(x)
# for i in reverse_twos_powers(10):
# 	print(i,end=", ")