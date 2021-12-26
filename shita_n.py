import math

def shita_n(p, r, shita):
    return -2 * math.asin(p / r) + shita

# p = float(input("今回の反射位置(mm) = "))
# r = float(input("曲率半径(mm) = "))
# shita = float(input("前回の反射角度(rad) = "))
# print(shita_n(p, r, shita))
