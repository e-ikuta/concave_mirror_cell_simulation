import math
from fractions import Fraction

def gamma_0(alpha_0, beta_0):
    return Fraction(math.asin((Fraction(1) - Fraction(math.sin(alpha_0))**2 - Fraction(math.sin(beta_0))**2)**0.5))

# alpha_0 = float(input("x軸入射角(度) = "))
# beta_0 = float(input("y軸入射角(度) = "))
# print(gamma_0(alpha_0, beta_0))
