import math

def a_n(gamma_prev):
    return (math.sin(gamma_prev))**(-2)

# gamma_prev = float(input("前回のz軸反射角 = "))
# print(a_n(gamma_prev))
