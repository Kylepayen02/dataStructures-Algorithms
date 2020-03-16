
import math 

def factors(num):
	for j in range(1,int(math.sqrt(num))):
		if num%j==0: 
			yield(j)
	for i in range((int(math.sqrt(num))),0,-1): 
		if num%i==0:
			yield(int(num/i))




