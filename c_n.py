import math
from fractions import Fraction

def c_n(x, alpha, y, beta, z, gamma, d, r, n):
    calc_1 = (Fraction(x) - Fraction(math.sin(alpha)) / Fraction(math.sin(gamma)) * Fraction(z))**2
    calc_2 = (Fraction(y) - Fraction(math.sin(beta)) / Fraction(math.sin(gamma)) * Fraction(z))**2
    calc_3 = ((Fraction(1) + Fraction((-1)**(n-1))) * Fraction(d) / Fraction(2) + Fraction((-1)**n) * Fraction(r))**2 - Fraction(r**2)
    return Fraction(calc_1) + Fraction(calc_2) + Fraction(calc_3)

# x = float(input("前回のx軸反射位置(mm) = "))
# alpha = float(input("前回のx軸反射角度(rad) = "))
# y = float(input("前回のy軸反射位置(mm) = "))
# beta = float(input("前回のy軸反射角度(rad) = "))
# z = float(input("前回のz軸反射位置(mm) = "))
# gamma = float(input("前回のz軸反射角度(rad) = "))
# d = float(input("ミラー間距離(mm) = "))
# r = float(input("曲率半径(mm) = "))
# n = float(input("反射回数 = "))
# print(c_n(x, alpha, y, beta, z, gamma, d, r, n))
