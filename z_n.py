import math

def z_n(a, b, c, gamma, n):
    return math.sin(gamma)**2 * (-b / 2 + (-1)**(n-1) * ((b / 2)**2 - a * c)**(0.5))

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
gamma = float(input("gamma = "))
n = float(input("n = "))
print(z_n(a, b, c, gamma, n))
