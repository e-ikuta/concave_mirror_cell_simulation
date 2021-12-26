input_file = input("入力ファイル名 = ")
output_file = input("出力ファイル名 = ")

import csv
import yaml

from a_n import a_n
from b_n import b_n
from c_n import c_n
from d_n import d_n
from degree_to_radian import degree_to_radian
from gamma_0 import gamma_0
from gamma_n import gamma_n
from p_n import p_n
from shita_n import shita_n
from z_0 import z_0
from z_n import z_n
from distance_from_mirror_center import distance_from_mirror_center

with open(input_file, 'r') as f:
    input = yaml.safe_load(f)

d = input['d']
r = input['r']
n = input['n']
x_0 = input['x_0']
alpha_0 = degree_to_radian(input['alpha_0'])
y_0 = input['y_0']
beta_0 = degree_to_radian(input['beta_0'])

x = x_0
alpha = alpha_0
y = y_0
beta = beta_0
z = z_0(r, x_0, y_0)
gamma = gamma_0(alpha_0, beta_0)
l = 0
i = 0

output = [['反射回数', '光路長(m)', '位置x(mm)', '位置y(mm)']]
output.append([i, l, x, y])
with open(output_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(output)

i += 1

while i <= n:
    a = a_n(gamma)
    b = b_n(x, alpha, y, beta, z, gamma, d, r, i)
    c = c_n(x, alpha, y, beta, z, gamma, d, r, i)
    z_after = z_n(a, b, c, gamma, i)
    dd = d_n(z, z_after, gamma)
    x_after = p_n(x, alpha, dd)
    alpha_after = shita_n(x_after, r, alpha)
    y_after = p_n(y, beta, dd)
    beta_after = shita_n(y_after, r, beta)
    gamma_after = gamma_n(alpha_after, beta_after, i)

    x = x_after
    alpha = alpha_after
    y = y_after
    beta = beta_after
    z = z_after
    gamma = gamma_after
    l += (dd / 1000)

    if distance_from_mirror_center(x, y) > 25:
        break

    with open(output_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerows([[i, l, x, y]])

    i += 1
