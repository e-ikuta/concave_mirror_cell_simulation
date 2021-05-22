import math

def d_n(z_before, z_after, gamma):
    return (z_after - z_before) / math.sin(gamma)

z_before = float(input("前回のz軸反射位置(mm) = "))
z_after = float(input("今回のz軸反射位置(mm) = "))
gamma = float(input("前回のz軸反射角度(rad) = "))
print(d_n(z_before, z_after, gamma))
