# Je dana elipsa v bazovych vektorech (1,0) a (0,1)
# (x-3)**2 / 4 + (y - 2)**2 / 9 = 1
# najdete predpis a graf v bazi (2,1), (-1, 4)

import numpy as np
import matplotlib.pyplot as plt

# stred a poloosy
x0 = 3
y0 = 2
a = 2
b = 3

v1 = np.array([2, 1])
v2 = np.array([-1, 4])

# 1) matice prechodu
M = np.column_stack((v1, v2))

# 2) soustava v bazovych vektorech
uhel = np.linspace(0, 2*np.pi, 1000) # uhel mezi 0 a 2 pi (rad)
ox = x0 + a*np.cos(uhel)
oy = y0 + b*np.sin(uhel)

# 3) linearni trasformace do nove baze
# body krivky nasobime matici M
puv_bod = np.vstack((ox, oy))
nov_bod = M @ puv_bod

x_trans = nov_bod[0,:]
y_trans = nov_bod[1,:]

# stred
puv_str = np.array([x0, y0])
nov_str = M @ puv_str

# 4) vykresleni grafu vedle sebe (vlevo puvodni, vpravo po transtofmaci)

fig = plt.figure(figsize=(16, 8))

ax1 = fig.add_subplot(121) # puvodni
ax2 = fig.add_subplot(122) # novy

ax1.plot(ox, oy, color='black', linewidth=3, label='Křivka před transformací', zorder=3,)
ax1.scatter(x0, y0, color='crimson', s=100, zorder=5, label=f'Střed S [{x0}, {y0}]',)

# Standardní bazové vektory v levém grafu ((1,0) a (0,1))
ax1.quiver(x0, y0, 1, 0, angles='xy', scale_units='xy', scale=1, color='blue', label=r'Báze $\mathbf{e}_1=(1,0)$',zorder=4,)
ax1.quiver(x0, y0, 0, 1, angles='xy', scale_units='xy', scale=1, color='green', label=r'Báze $\mathbf{e}_2=(0,1)$', zorder=4,)

# puvodni, baze (1,0) a (0,1)
ax1.set_xlim(x0-a-3, x0+a+3)
ax1.set_ylim(y0-b-3, y0+b+3)

ax1.set_xlabel('Osa X', fontsize=11)
ax1.set_ylabel('Osa Y', fontsize=11)
ax1.set_title(rf"Původní báze: $\frac{{(x-{x0})^2}}{{{a**2}}} + \frac{{(y-{y0})^2}}{{{b**2}}} = 1$", fontsize=12, pad=10,)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper right')
ax1.set_aspect('equal')

# nova, transformovana elipsa
ax2.plot(x_trans, y_trans, color='black', linewidth=3, label='Křivka po transformací',zorder=4,)
ax2.scatter(nov_str[0], nov_str[1], color='crimson', s=100, zorder=5, label=f"Transformovaný střed S [{nov_str[0]:.2f}, {nov_str[1]:.2f}]",)

# bazove vektory
ax2.quiver(nov_str[0], nov_str[1], v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label=r'Nová osa $\mathbf{v}_1 = ' + str(list(v1)) + r'$', zorder=4,)
ax2.quiver(nov_str[0], nov_str[1], v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='green', label=r'Nová osa $\mathbf{v}_2 = ' + str(list(v2)) + r'$', zorder=4,)

ax2.set_xlim(np.min(x_trans) - 3, np.max(x_trans) + 3)
ax2.set_ylim(np.min(y_trans) - 3, np.max(y_trans) + 3)

# matice do nadpisu

ax2.set_xlabel("Transformovaná osa X'", fontsize=11)
ax2.set_ylabel("Transformovaná osa Y'", fontsize=11)
ax2.set_title(rf"Nová báze: $\frac{{(x-{nov_str[0]:.1f})^2}}{{{a**2}}} + \frac{{(y-{nov_str[1]:.1f})^2}}{{{b**2}}} = 1$", fontsize=12, pad=10,)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
ax2.set_aspect('equal')


plt.tight_layout(rect=[0, 0, 1, 0.90])

plt.suptitle(f"Křivka po transformaci M = ({v1}, {v2})")
plt.show()