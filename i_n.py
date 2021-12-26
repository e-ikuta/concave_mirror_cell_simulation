import math

def i_n(i, shita, d_n):
    return i + d_n * math.sin(shita)

# i = float(input("前回の反射位置(mm) = "))
# shita = float(input("前回の反射角度(rad) = "))
# d_n = float(input("今回の光路長(mm) = "))
# print(i_n(i, shita, d_n))
