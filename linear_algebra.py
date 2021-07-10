''' Matrix
    The class is initiated by a list of vectors. The vectors much be of equal length for every row and they must all contain
    either a float or an int. The matrix contains built in functions like is_qudratic, which returns a boolean pertaining to
    whether or nor the matrix is of a quadratic form or not. Moreover the matrix also contains a function that returns the transponate
    of the matrix, that is, the rows turned into columns and the columns turned into rows.
'''

class matrix:
    def __init__(self, m):
        assert len(m) > 0, "You cannot assign a matrix an empty list."
        self.rows = len(m)
        self.cols = len(m[0])
        self.quadratic = True
        self.vectors = []

        if(not self.cols == self.rows):
            self.quadratic = False

        for i in range(0,self.rows):
            assert len(m[i]) == self.cols, "You cannot load in different amounts of colums for different rows, see row %d" %i
            self.vectors.append(m[i])

    def is_quadratic(self):
        return self.quadratic

    def transponate(self):
        l = []
        for i in range(self.rows):
            l.append([])
            for j in range(self.cols):
                l[i].append(self.vectors[j][i])
        return matrix(l)

''' Dot Product
    Dot Product is defined as the sum of all the products of two vectors. This dot product is geometrically very important,
    for instance it can be used to determine orthogonality between two vectors which is used later on aswell. Dot Product
    is a simple procedure, we simply sum up all the products pairwise and return it.
'''

def dot_product(v1,v2):
    l1 = len(v1)
    l2 = len(v2)
    assert l1 == l2, "Unequal lengths of vectors!"
    numeric_datatypes = [int,float]
    sum = 0

    for i in range(l1):
        a = v1[i]
        b = v2[i]

        assert type(a) in numeric_datatypes, "Vector A has on index %d a wrongful datatype (not int or float)" % i
        assert type(b) in numeric_datatypes, "Vector B has on index %d a wrongful datatype (not int or float)" % i
        sum += a*b

    return sum

assert dot_product([4,4,4],[4,4,4]) == 48

''' is_orthogonal
    Using the aforementioned function "dot_product" we implement it as a boolean function to see if two vectors are
    orthogonal. For instance, the base vectors [1,0,0], [0,1,0], [0,0,1] are naturally orthogonal and perpendicular as
    their dot product will amount to 0.  
'''
def is_orthogonal(v1, v2):
    if(dot_product(v1,v2) == 0):
        return True
    return False

assert is_orthogonal([1,0,0], [0,0,1])

''' cross_product
    Cross product is defined in 3D space, the crossproduct of two vectors that we must call v1 and v2 will amount to a
    third vector called v3 which is perpendicular to the plane that v1 and v2 spans. V3 in this case is to be refered to
    as the normal vector of that plane. To make a cross product see the return statement below:
'''
def cross_product(v1,v2):
    l1 = len(v1)
    l2 = len(v2)
    assert l1 == l2,      "Unequal sizes of vectors!"
    assert l1 == l2 == 3, "Cross Product should be defined in 3D space!"
    numeric_datatypes = [int, float]

    for i in range(3):
        assert type(v1[i]) in numeric_datatypes, "Vector A has to be of a numeric datatype!"
        assert type(v2[i]) in numeric_datatypes, "Vector B has to be of a numeric datatype!"

    return [(v1[1]*v2[2] - v1[2]*v2[1]), (v1[2]*v2[0] - v2[2]*v1[0]), (v1[0]*v2[1] - v1[1]*v2[0])]

assert cross_product([0,1,0],[1,0,0]) == [0,0,-1]

''' scalar_product
    Another common form of products is the scalar, it simply means that we take a scaling constant and apply that to all
    the elements inside the vector.
'''
def scalar_product(scalar, v):
    return list(map (lambda e : e*scalar, v))

assert scalar_product(5,[1,2,3,4,5]) == [5,10,15,20,25]

m1 = matrix([[1,2],[3,4]])
m1_t = m1.transponate()
assert m1_t.vectors[0] == [1,3]
assert m1_t.vectors[1] == [2,4]
m1_t_t = m1_t.transponate()
assert m1.vectors[0] == m1_t_t.vectors[0]
assert m1.vectors[1] == m1_t_t.vectors[1]

def matrix_multiplication(m1,m2):
    c2 = m2.transponate()
    l = []
    for i in range(m1.rows):
        l.append([])
        for j in range(m2.rows):
            v1 = m1.vectors[i]
            v2 = c2.vectors[j]
            e = dot_product(v1,v2)
            l[i].append(e)

    return matrix(l)

M1 = matrix([[1,2],[3,4]])
M2 = matrix([[1,2],[3,4]])

M3 = matrix_multiplication(M1,M2)
assert M3.vectors[0] == [7,10]
assert M3.vectors[1] == [15,22]
