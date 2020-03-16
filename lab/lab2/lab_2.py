#1 

class polynomial: 
	def __init__(self, coefficient_lst): 
		self.coefficient_lst = coefficient_lst

	def __add__(self,poly2): 
		lst = [] 
		if len(poly2.coefficient_lst)>len(self.coefficient_lst): 
			for i in range(len(self.coefficient_lst)): 
				lst.append((self.coefficient_lst[i]+poly2.coefficient_lst[i]))
			for j in range(len(self.coefficient_lst), len(self.coefficient_lst)+(len(poly2.coefficient_lst)-len(self.coefficient_lst))):
				lst.append(poly2.coefficient_lst[j])
		else: 
			for i in range(len(poly2.coefficient_lst)): 
				lst.append((self.coefficient_lst[i]+poly2.coefficient_lst[i]))
			for j in range(len(poly2.coefficient_lst), len(poly2.coefficient_lst)+(len(self.coefficient_lst)-len(poly2.coefficient_lst))):
				lst.append(self.coefficient_lst[j])
		return polynomial(lst)

	def __call__(self,n):
		count = 0
		total = 0 
		for i in self.coefficient_lst: 
			total += (n**count)*i
		return total 

poly1 = polynomial([3,7,0,-9,2])
poly2 = polynomial([2,0,0,5,0,0,3])
poly3 = poly1+poly2 
print(poly3.coefficient_lst)


	

