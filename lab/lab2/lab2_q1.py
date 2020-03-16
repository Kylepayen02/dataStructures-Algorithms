class Polynomial:
    def __init__(self,lst=[0]):
        self.coefficient = lst
    def __add__(self, poly2):
        res = []
        if len(self.coefficient) >= len(poly2.coefficient):
            for i in range(len(poly2.coefficient)):
                res.append(self.coefficient[i] + poly2.coefficient[i])
            for k in range(len(poly2.coefficient), len(self.coefficient)):
                res.append(self.coefficient[k])
        else:
            for j in range(len(self.coefficient)):
                res.append(self.coefficient[j] + poly2.coefficient[j])
            for l in range(len(self.coefficient), len(poly2.coefficient)):
                res.append(poly2.coefficient[l])
        return Polynomial(res)
    def __call__(self, n):
        total = 0
        count = 0
        for i in self.coefficient:
            total += i * (n**count)
            count+=1
        return total
    def __repr__(self):
        count = len(self.coefficient)-1
        my_poly = ''
        for i in range(len(self.coefficient)-1,-1,-1):
            if i != 0:
                my_poly += str(self.coefficient[i])+"x^"+str(i)+ " + "
            else:
                my_poly += str(self.coefficient[i]) + "x^" + str(i)

        return my_poly
    

poly3 = Polynomial([3,7,0,-9,2])
poly4 = Polynomial([2,0,0,5,0,0,3])
poly5 = poly3+poly4
# print(poly5.coefficient)
vall = poly5(1)
print(poly3)






