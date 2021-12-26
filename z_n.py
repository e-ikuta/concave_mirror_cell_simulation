import math
from fractions import Fraction

def z_n(a, b, c, gamma, n):
    return Fraction(math.sin(gamma)**2) * (Fraction(-b) / Fraction(2) + Fraction((-1)**(n-1)) * Fraction((b / 2)**2 - a * c)**(0.5))

# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# gamma = float(input("gamma = "))
# n = float(input("n = "))
# print(z_n(a, b, c, gamma, n))
