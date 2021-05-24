import math
import yaml

with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

d = float(config['d'])
r = float(config['r'])
n = float(config['n'])
x_0 = float(config['x_0'])
alpha_0 = math.radians(float(config['alpha_0']))
y_0 = float(config['y_0'])
beta_0 = math.radians(float(config['beta_0']))

def gamma_0(alpha_0, beta_0):
    return math.asin((1 - (math.sin(alpha_0))**2 - (math.sin(beta_0))**2)**0.5)

def z_0(r, x_0, y_0):
    return r - (r**2 - x_0**2 - y_0**2)**0.5

def a_n(gamma):
    return (math.sin(gamma))**(-2)

def b_n(x, alpha, y, beta, z, gamma, d, r, n):
    calc_1 = (x * math.sin(alpha) + y * math.sin(beta)) / math.sin(gamma)
    calc_2 = (1 - 1 / math.sin(gamma)**2) * z
    calc_3 = -((1 + (-1)**(n-1)) * d / 2 + (-1)**n * r)
    return (calc_1 + calc_2 + calc_3) * 2

def c_n(x, alpha, y, beta, z, gamma, d, r, n):
    calc_1 = (x - math.sin(alpha) / math.sin(gamma) * z)**2
    calc_2 = (y - math.sin(beta) / math.sin(gamma) * z)**2
    calc_3 = ((1 + (-1)**(n-1)) * d / 2 + (-1)**n * r)**2 - r**2
    return calc_1 + calc_2 + calc_3

def z_n(a, b, c, gamma, n):
    return math.sin(gamma)**2 * (-b / 2 + (-1)**(n-1) * ((b / 2)**2 - a * c)**(0.5))

def d_n(z_before, z_after, gamma):
    return (z_after - z_before) / math.sin(gamma)

def i_n(i, shita, d_n):
    return i + d_n * math.sin(shita)

def shita_n(i, shita, r):
    return -2 * math.asin(i / r) + shita

def gamma_n(alpha, beta, n):
    return math.asin((1 - math.sin(alpha)**2 - math.sin(beta)**2)**0.5) / (-1)**(n)

# x軸入射位置(mm)
x = x_0
# x軸入射角度(rad)
alpha = alpha_0
# y軸入射位置(mm)
y = y_0
# y軸入射角度(rad)
beta = beta_0
# z軸入射位置(mm)
z = z_0(r, x_0, y_0)
# z軸入射角度(rad)
gamma = gamma_0(alpha_0, beta_0)
# 反射回数
i = 1

while i <= n:
    print(i)

    a = a_n(gamma)
    b = b_n(x, alpha, y, beta, z, gamma, d, r, i)
    c = c_n(x, alpha, y, beta, z, gamma, d, r, i)
    z_after = z_n(a, b, c, gamma, i)
    dd = d_n(z, z_after, gamma)
    x_after = i_n(x, alpha, dd)
    alpha_after = shita_n(x_after, alpha, r)
    y_after = i_n(y, beta, dd)
    beta_after = shita_n(y_after, beta, r)
    gamma_after = gamma_n(alpha_after, beta_after, i)

    x = x_after
    alpha = alpha_after
    y = y_after
    beta = beta_after
    z = z_after
    gamma = gamma_after
    i += 1

    print(f"x: {x}")
    print(f"alpha: {alpha}")
    print(f"y: {y}")
    print(f"beta: {beta}")
    print(f"z: {z}")
    print(f"gamma: {gamma}")
