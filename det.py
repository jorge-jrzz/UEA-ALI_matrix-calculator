# import numpy as np
# import sympy as sp

# C = sp.Matrix([[1,   2,   3],
#               [4,   5,   6],
#               [7,   8,   9]])

# if C.det() == 0:
#     print("siiiiiiii")


from fractions import Fraction
import numpy as np

a = 1/3
b = Fraction(str(a))
print('Valor de b: ', b)

c = Fraction(str(a)).limit_denominator()
print('Valor de c: ', c)


matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

mat = np.array(matriz1)

print(type(mat))
