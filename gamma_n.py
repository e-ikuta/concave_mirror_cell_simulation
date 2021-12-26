import math
from fractions import Fraction

def gamma_n(alpha, beta, n):
    return Fraction(math.asin((Fraction(1) - Fraction(math.sin(alpha))**2 - Fraction(math.sin(beta))**2)**0.5) / Fraction((-1)**(n)))

# alpha = float(input("今回のx軸反射角度(rad) = "))
# beta = float(input("今回のy軸反射角度(rad) = "))
# n = float(input("反射回数 = "))
# print(gamma_n(alpha, beta, n))
