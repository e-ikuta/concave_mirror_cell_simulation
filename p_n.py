import math

def p_n(p, shita, d_n):
    return p + d_n * math.sin(shita)

# p = float(input("前回の反射位置(mm) = "))
# shita = float(input("前回の反射角度(rad) = "))
# d_n = float(input("前回の反射から今回の反射までの距離(mm) = "))
# print(p_n(p, shita, d_n))
