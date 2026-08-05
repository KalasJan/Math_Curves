# Vykreslete Elipsu polarne i po (ne)linearni transformaci, ktera je dana matici
# np.array([[1, np.sin(x)],[np.cos(x)2,1]])
# obrazky dejte vedle sebe

import numpy as np
import matplotlib.pyplot as plt

# stred a poloosy
x0 = 2
y0 = 3
a = 3
b = 4

# 1) pres polarni system
uhel = np.linspace(0, 2*np.pi, 1000) # uhel mezi 0 a 2 pi (rad)

# soustava
ox = x0 + a*np.cos(uhel)
oy = y0 + b*np.sin(uhel)

# ============================================================

# (ne)linearni transformace

# prazdna pole pro transformaci
trans_x = np.zeros_like(ox)
trans_y = np.zeros_like(oy)

# transformace x_nove = M * x_stare
for i in range(len(uhel)):
    xi = ox[i]
    yi = oy[i]
    
    # matice transformace
    def M(p):
        return np.array([[1,np.sin(p)],
                         [np.cos(p),1]])

# prepocet na nove souradnice
    nove = M(xi) @ np.array([xi, yi])
    trans_x[i] = nove[0]
    trans_y[i] = nove[1]

stred_novy = M(x0) @ np.array([x0, y0])

# ==================================================

# vykresleni grafu vedle sebe (vlevo puvodni, vpravo po transtofmaci)

fig = plt.figure(figsize=(16, 8))

# Levý, původní graf
ax1 = fig.add_subplot(121)
ax1.plot(ox, oy, color='black', linewidth=3, label='Graf před transformací', zorder=3)
ax1.scatter(x0, y0, color='crimson', s=100, zorder=4, label=f'Střed S[{x0}, {y0}]')

ax1.axhline(y0, color='blue', linewidth=0.8, linestyle='--', alpha=0.5)
ax1.axvline(x0, color='green', linewidth=0.8, linestyle='--', alpha=0.5)

ax1.set_xlim(-3, 7)
ax1.set_ylim(-3, 9)
ax1.set_xlabel('Osa X', fontsize=11)
ax1.set_ylabel('Osa Y', fontsize=11)
ax1.set_title(fr'A) Kartézsky: $\frac{{(x-{x0})^2}}{{{a}^2}} + \frac{{(y-{y0})^2}}{{{b}^2}} = 1$', fontsize=12, pad=10)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend()
ax1.set_aspect('equal')


# Pravý graf, po transforaci danou maticí M
ax2 = fig.add_subplot(122)
ax2.plot(trans_x, trans_y, color='black', linewidth=3, label='Graf po (ne)lineární transformaci', zorder=3)
ax2.scatter(stred_novy[0], stred_novy[1], color='crimson', s=100, zorder=4, 
            label=f'Transformovaný střed S [{stred_novy[0]:.2f}, {stred_novy[1]:.2f}]')

# Pomocné nulové osy - i po transfformaci budou kolme
# ax2.axhline(stred_novy[1], color='gray', linewidth=0.8, linestyle='--', alpha=0.5)
# ax2.axvline(stred_novy[0], color='gray', linewidth=0.8, linestyle='--', alpha=0.5)

# zakriveni hlavnich os
rozsah = np.linspace(-20,20,1000)

osa1_x, osa1_y = np.zeros_like(rozsah), np.zeros_like(rozsah)
osa2_x, osa2_y = np.zeros_like(rozsah), np.zeros_like(rozsah)

for j in range(len(rozsah)):
    value = rozsah[j]
    
    # transformace osy x (y = 0)
    novy_x = M(value) @ np.array([value, y0])
    osa1_x[j], osa1_y[j] = novy_x[0], novy_x[1]
    
    # transformace osy y (x = 0)
    novy_y = M(x0) @ np.array([x0, value])
    osa2_x[j], osa2_y[j] = novy_y[0], novy_y[1]

# zakresleni pokrivenych os
ax2.plot(osa1_x, osa1_y, color='blue', linewidth=1.2, linestyle='--', alpha=0.6, label='Zakřivená osa X\'')
ax2.plot(osa2_x, osa2_y, color='green', linewidth=1.2, linestyle='--', alpha=0.6, label='Zakřivená osa Y\'')

ax2.set_xlim(np.min(trans_x) - 2, np.max(trans_x) + 2)
ax2.set_ylim(np.min(trans_y) - 2, np.max(trans_y) + 2)

ax2.set_xlabel('Deformovaná osa X\'', fontsize=11)
ax2.set_ylabel('Deformovaná osa Y\'', fontsize=11)
ax2.set_title(r'Po (ne)lineární transformaci maticí $M(x)$', fontsize=12, pad=10)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend()
ax2.set_aspect('equal')

# Globální titulek celého dashboardu
plt.suptitle(r'(Ne)lineární deformace geometrického útvaru', fontsize=15, weight='bold', y=0.96)
plt.tight_layout()
plt.show()
