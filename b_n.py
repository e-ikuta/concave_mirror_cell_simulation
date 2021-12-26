import math

def b_n(x, alpha, y, beta, z, gamma, d, r, n):
    calc_1 = (x * math.sin(alpha) + y * math.sin(beta)) / math.sin(gamma)
    calc_2 = (1 - 1 / math.sin(gamma)**2) * z
    calc_3 = -((1 + (-1)**(n-1)) * d / 2 + (-1)**n * r)
    return (calc_1 + calc_2 + calc_3) * 2

# x = float(input("前回のx軸反射位置(mm) = "))
# alpha = float(input("前回のx軸反射角度(rad) = "))
# y = float(input("前回のy軸反射位置(mm) = "))
# beta = float(input("前回のy軸反射角度(rad) = "))
# z = float(input("前回のz軸反射位置(mm) = "))
# gamma = float(input("前回のz軸反射角度(rad) = "))
# d = float(input("ミラー間距離(mm) = "))
# r = float(input("曲率半径(mm) = "))
# n = float(input("反射回数 = "))
# print(b_n(x, alpha, y, beta, z, gamma, d, r, n))
