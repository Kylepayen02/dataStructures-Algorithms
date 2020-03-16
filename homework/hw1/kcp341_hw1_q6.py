class Vector:
	def __init__(self, d):
		x = isinstance(d,int)
		if x == False:
			self.coords = d
		else:
			self.coords = [0]*d
	def __len__(self):
		return len(self.coords)
	def __getitem__(self, j):
		return self.coords[j]
	def __setitem__(self, j, val):
		self.coords[j] = val
	def __add__(self, other):
		if len(self) != len(other):
			raise ValueError("dimensions must agree")
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		return result
	def __sub__(self,other): 
		if len(self) != len(self):
			raise ValueError("dimensions must agree")
		res = Vector(len(self))
		for j in range(len(self)):
			res[j] = self[j] - other[j]
		return res
	def __neg__(self): 
		res = Vector(len(self))
		for i in range(len(self)):
			res[i] = self[i] * -1
		return res
	def __mul__(self, other): 
		x = isinstance(other,int)
		if x==False:
			res = 0
			for i in range(len(self)):
				res += self[i] * other[i]
			return res
		else:
			res = Vector(len(self))
			for i in range(len(self)):
				res[i] = self[i] * other
			return res

	def __rmul__(self,other): 
		res = Vector(len(self))
		for i in range(len(self)):
			res[i] = other*self[i]
		return res

	def __eq__(self, other):
		return self.coords == other.coords
	def __ne__(self, other):
		return not (self == other)
	def __str__(self):
		return '<'+ str(self.coords)[1:-1] + '>'
	def __repr__(self):
		return str(self)

