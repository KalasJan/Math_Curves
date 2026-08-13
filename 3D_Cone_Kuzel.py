# Nakresli kužel

import numpy as np
import matplotlib.pyplot as plt

# stred a poloosy
x0 = 2
y0 = 3
z0 = 1
R1 = 3 # polomer osy x
R2 = 5 # polomer osy y
v = 6 # vyska

# sfericke souradnice
uhel = np.linspace(0, 2 * np.pi, 100)  # azimut (0 až 2pi)
polar = np.linspace(0, v, 100) # od podstavy po vrchol
U, P = np.meshgrid(uhel, polar)

# rovnice
akt = (1 - P / v)

xku = x0 + R1 * akt * np.cos(U)
yku = y0 + R2 * akt * np.sin(U)
zku = z0 + P

# kresleni
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(xku, yku,zku, cmap='summer', edgecolor='none', alpha=0.85,)
ax.set_title(rf'Kužel: $\frac{{(x-{x0})^2}}{{{R1}^2}} + \frac{{(y-{y0})^2}}{{{R2}^2}} = \frac{{(z-{z0})^2}}{{{v}^2}}$', fontsize=11,)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.axis('equal')

plt.tight_layout()
plt.show()