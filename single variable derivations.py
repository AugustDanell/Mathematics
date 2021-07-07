class polynomial:
    def __init__(self, L):
        self.polyList = L
        self.highest_degree = len(L)

    def derivative(self):
        dl = []
        for i in range(1,self.highest_degree):
            dl.append(self.polyList[i]*i)

        self.polyList = dl
        self.highest_degree -= 1

        if(len(dl) == 1):
            self.polyList = dl[0]

p = polynomial([1,2,3])
p.derivative()
assert p.polyList == [2,6], "Polynomial Derivation is NOT ok!"
p.derivative()
assert p.polyList == 6, "When reduced to only a constant term we should return that constant term!"
p.derivative()
assert p.polyList == [], "We need to derive away the function."

class euler_function:
    def __init__(self,c,ex):
        self.coefficient = c
        self.exponent = ex
        self.derivation = polynomial(ex.polyList)
        self.derivation.derivative()

    def derivative(self):
        self.coefficient *= self.derivation.polyList

    def primitive_function(self):
        self.coefficient /= self.derivation.polyList

p1 = polynomial([0,6])
e = euler_function(5,p1)
print(e.coefficient)
e.derivative()
assert e.coefficient == 30
e.derivative()
assert e.coefficient == 180
e.primitive_function()
assert e.coefficient == 30