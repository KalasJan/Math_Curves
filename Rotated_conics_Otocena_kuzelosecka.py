# Vykreslete kuzelosecku obecnou kuzelosexku

import numpy as np
import matplotlib.pyplot as plt
import sympy as sm

A = 1
B = 6
C = 3
D = 2
E = 4
F = 6

# definice funkce
def Z(X,Y):
    return A*(X**2) + C*(Y**2) + B*(X*Y) + D*X + E*Y + F 

# mriz na kresleni
x_num = np.linspace(-10, 10, 1000)
y_num = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x_num, y_num)

# ====================================================

# 1) vypocet stredu
xs, ys = sm.symbols('x y')
Zs = A*(xs**2) + C*(ys**2) + B*(xs*ys) + D*xs + E*ys + F 


grad_x = sm.diff(Zs, xs)
grad_y = sm.diff(Zs, ys)

stred_sol = sm.solve([grad_x, grad_y], (xs, ys))
stred_x = float(stred_sol[xs])
stred_y = float(stred_sol[ys])

print(f"Střed kuželosečky S: [{stred_x:.2f}, {stred_y:.2f}]")

# ===========================================

# 2) maticova analyza (NumPy))
# obecny predpis je Ax^2 + Bxy + Cx^2 +Dx + Ey + F = 0
# M = [[A, B/2], [B/2, C]]

M = [[A, B/2], [B/2, C]]

# vlastni cisla a vektory
vlastni_cisla, vlastni_vektory = np.linalg.eigh(M)

vektor_osa_x = vlastni_vektory[:, 0] # Směr hlavní osy
vektor_osa_y = vlastni_vektory[:, 1] # Směr vedlejší osy (kolmé)

# vypocet rotace
uhel_rad = np.arctan2(vektor_osa_x[1], vektor_osa_x[0])
uhel_deg = np.degrees(uhel_rad)
print(f"Úhel otočení: {uhel_deg:.1f}°\n")

# =================================================

# 3) Kresleni grafu
plt.figure(figsize=(8, 8))

# zakladni osy, x = 0, y = 0
plt.axhline(0, color='gray', linewidth=0.8, linestyle= '--', alpha=0.5)
plt.axvline(0, color='gray', linewidth=0.8, linestyle= '--', alpha=0.5)

# otocene osy
t = np.linspace(-15, 15, 100)
osa1_x = stred_x + t * vektor_osa_x[0]
osa1_y = stred_y + t * vektor_osa_x[1]

osa2_x = stred_x + t * vektor_osa_y[0]
osa2_y = stred_y + t * vektor_osa_y[1]

plt.plot(osa1_x, osa1_y, color='crimson', linewidth=1.2, linestyle='-.', alpha=0.8, label='Hlavní osa (vlastní směr)')
plt.plot(osa2_x, osa2_y, color='royalblue', linewidth=1.2, linestyle='-.', alpha=0.8, label='Vedlejší osa (vlastní směr)')

# stred
plt.scatter(stred_x, stred_y, color='black', s=100, zorder=5, label=f'Střed $S$ [{stred_x:.1f}, {stred_y:.1f}]')

# kuzelosecka
plt.contour(X, Y, Z(X,Y), levels=[0], colors='Red', linewidths=2.5)

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axis('equal') # kvuli nedeformaci
plt.xlabel('Osa X', fontsize=11)
plt.ylabel('Osa Y', fontsize=11)
plt.title(rf'Obecná kuželosečka: ${A}x^2 + {B}xy + {C}y^2 + {D}x + {E}y + {F} = 0$', fontsize=12, weight='bold', pad=15)
plt.grid(True, linestyle=':', alpha=0.4)
plt.legend(loc = 'lower left')

plt.show()