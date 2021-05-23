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

# z軸入射位置(mm)
z_0 = z_0(r, x_0, y_0)
# z軸入射角度(rad)
gamma_0 = gamma_0(alpha_0, beta_0)

a_1 = a_n(gamma_0)
b_1 = b_n(x_0, alpha_0, y_0, beta_0, z_0, gamma_0, d, r, 1)
c_1 = c_n(x_0, alpha_0, y_0, beta_0, z_0, gamma_0, d, r, 1)
z_1 = z_n(a_1, b_1, c_1, gamma_0, 1)
d_1 = d_n(z_0, z_1, gamma_0)
x_1 = i_n(x_0, alpha_0, d_1)
alpha_1 = shita_n(x_1, alpha_0, r)
y_1 = i_n(y_0, beta_0, d_1)
beta_1 = shita_n(y_1, beta_0, r)
gamma_1 = gamma_n(alpha_1, beta_1, 1)

print(f"x_1: {x_1}")
print(f"alpha_1: {alpha_1}")
print(f"y_1: {y_1}")
print(f"beta_1: {beta_1}")
print(f"z_1: {z_1}")
print(f"gamma_1: {gamma_1}")
