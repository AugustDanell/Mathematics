import math

class euler:
    def __init__(self,constant,expo):
        self.base = math.e
        self.coff = constant

class polynomial:
    def __init__(self, L):
        self.polyList = L
        self.highest_degree = len(L)

    def value_of_poly_at(self,x):
        s = 0
        for i in range(self.highest_degree):
            c = self.polyList[i]
            s += c*x**i
        return s

# TODO
class function:
    def __init__(self):
        self.constant = 0
        self.operator = ""
        self.function_list = []

    def reading_in_function(self, input_string):
        function_split = input_string.split(" ")
        operations = ["+", "-", "/", "*"]
        negative = False
        local_list = []
        constant = 0.
        for i in function_split:

            if(i == "+"):
                self.function_list.append(local_list)
            elif(i == "-"):
                self.function_list.append(local_list)
                negative = True

            if(local_list == []):
                local_list.append(negative)

            if(i.isnumeric()):
                constant = float(i)
            else:
                constant = 0.

def almost_equal(x,y,threshhold):
    return abs(x-y) < threshhold

p = polynomial([1,2,3]) # -> f(x) = 1 + 2x + 3x^2, f'(x)= 2 + 6x.
assert p.value_of_poly_at(1) == 6   # f(1) =  6.
assert p.value_of_poly_at(2) == 17  # f(2) =  17.
assert p.value_of_poly_at(-2) == 9  # f(-2) = 9.

def polynomial_derivation_CD(poly, x, h = 10**-6):
    return (poly.value_of_poly_at(x+h) - poly.value_of_poly_at(x-h))/2*h

# f'(x) = 2 + 6x
print(polynomial_derivation_CD(p,1))
#assert almost_equal(polynomial_derivation_CD(p,1),8,0.01)


