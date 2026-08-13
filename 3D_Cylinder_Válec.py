# Nakresli Elipticky, Rotacni, Hyperbolicky a Parabolicky valec

import numpy as np
import matplotlib.pyplot as plt

# stred a poloosy
x0 = 2
y0 = 3
z0 = 1 # spodni hranice
z1 = 3 # horni hranice
a = 2
b = 7
c = 2

x = np.linspace(0, 2 * np.pi, 500) # parametrizace pro elipticky a rotacni valec
y = np.linspace(z0, z1, 500)
X,Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(14, 12))
ax1 = fig.add_subplot(221, projection='3d')
ax2 = fig.add_subplot(222, projection='3d')
ax3 = fig.add_subplot(223, projection='3d')
ax4 = fig.add_subplot(224, projection='3d')

# 1) Elipticky
xe = x0 + a * np.cos(x)
ye = y0 + b * np.sin(x)

# kresleni
ax1.plot_surface(xe, ye, Y, cmap='Blues', edgecolor='none', alpha=0.8)
ax1.set_title(rf'Eliptický válec: $\frac{{(x-{x0})^2}}{{{a}^2}} + \frac{{(y-{y0})^2}}{{{b}^2}} = 1$')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.axis('equal')


# 2) Rotacni
xr = x0 + a * np.cos(x)
yr = y0 + a * np.sin(x)

ax2.plot_surface(xr, yr, Y, cmap='Greens', edgecolor='none', alpha=0.8)
ax2.set_title(rf'Rotační válec, $\frac{{(x-{x0})^2}}{{{a}^2}} + \frac{{(y-{y0})^2}}{{{a}^2}} = 1$')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.axis('equal')


# 3) Hyperbolicky
t = np.linspace(y0 - 4, y0 + 4, 100)
Z_hyp, Y_h = np.meshgrid(y, t)

xh1 = x0 + a * np.sqrt(1 + ((Y_h - y0)**2) / (b**2))
xh2 = x0 - a * np.sqrt(1 + ((Y_h - y0)**2) / (b**2))

ax3.plot_surface(xh1, Y_h, Z_hyp, cmap='Oranges', edgecolor='none', alpha=0.8)
ax3.plot_surface(xh2, Y_h, Z_hyp, cmap='Reds', edgecolor='none', alpha=0.8)
ax3.set_title(rf'Hyperbolický válec, $\frac{{(x-{x0})^2}}{{{a}^2}} - \frac{{(y-{y0})^2}}{{{a}^2}} = 1$')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')
ax3.axis('equal')

# 4) Parabolicky
xp = np.linspace(x0 - 4, x0 + 4, 100)
zp, Xp = np.meshgrid(y, xp)
p = 3
yp = y0 + ((Xp - x0)**2)/ (2*p)

ax4.plot_surface(Xp, yp, zp, cmap='rainbow_r', edgecolor='none', alpha=0.8)
ax4.set_title(rf'Parabolický válec: $(y-{y0}) = \frac{{(x-{x0})^2}}{{{2*p}}}$')
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_zlabel('z')
ax4.axis('equal')


plt.suptitle('3D kuželosečka/kvadrika - Válec', fontsize=14)
plt.tight_layout()
plt.show()