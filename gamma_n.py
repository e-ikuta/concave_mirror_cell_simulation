import math

def gamma_n(alpha, beta, n):
    return math.asin((1 - math.sin(alpha)**2 - math.sin(beta)**2)**0.5) / (-1)**(n)

alpha = float(input("今回のx軸反射角度(rad) = "))
beta = float(input("今回のy軸反射角度(rad) = "))
n = float(input("反射回数 = "))
print(gamma_n(alpha, beta, n))
