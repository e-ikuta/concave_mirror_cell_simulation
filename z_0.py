def z_0(r, x_0, y_0):
    return r - (r**2 - x_0**2 - y_0**2)**0.5

r = float(input("曲率半径(mm) = "))
x_0 = float(input("x軸入射位置(mm) = "))
y_0 = float(input("y軸入射位置(mm) = "))
print(z_0(r, x_0, y_0))
