# Nakresli Elipsoid a Kouli (v polarnich i kartezskych souradnicich)

import numpy as np
import matplotlib.pyplot as plt

# stred a poloosy
x0 = 2
y0 = 3
z0 = 1
a = 2
b = 7
c = 2
r = 3 # polomer koule

# sfericke souradnice
uhel = np.linspace(0, 2 * np.pi, 100)  # azimut (0 až 2pi)
polar = np.linspace(0, np.pi, 50) # polární úhel (0 až pi)
U, P = np.meshgrid(uhel, polar)

# kartezsky system
xkar = np.linspace(x0 - a, x0 + a, 100)
ykar = np.linspace(y0 - b, y0 + b, 100)
Xkar, Ykar = np.meshgrid(xkar, ykar)

fig = plt.figure(figsize=(14, 12))
ax1 = fig.add_subplot(221, projection='3d')
ax2 = fig.add_subplot(222, projection='3d')
ax3 = fig.add_subplot(223, projection='3d')
ax4 = fig.add_subplot(224, projection='3d')

# 1) Elipsoid kartezsky
ek = 1 - ((Xkar - x0)**2)/(a**2) - ((Ykar - y0)**2)/(b**2)
ek[ek < 0] = np.nan  # ořezat mimo elipsu

ek1 = z0 + c * np.sqrt(ek)
ek2 = z0 - c * np.sqrt(ek)

ax1.plot_surface(Xkar, Ykar, ek1, cmap='Blues', edgecolor='none', alpha=0.8)
ax1.plot_surface(Xkar, Ykar, ek2, cmap='Blues', edgecolor='none', alpha=0.8)
ax1.set_title(rf'Elipsoid (kartézsky): $\frac{{(x-{x0})^2}}{{{a}^2}} + \frac{{(y-{y0})^2}}{{{b}^2}} + \frac{{(z-{z0})^2}}{{{c}^2}} = 1$')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.axis('equal')

# 2) Elipsoid polarne
xep = x0 + a * np.sin(P) * np.cos(U)
yep = y0 + b * np.sin(P) * np.sin(U)
zep = z0 + c * np.cos(P)

ax2.plot_surface(xep, yep, zep, cmap='Greens', edgecolor='none', alpha=0.8)
ax2.set_title(rf'Elipsoid (polárně): $x={x0}+{a}\sin\varphi\cos\theta,\ y={y0}+{b}\sin\varphi\sin\theta,\ z={z0}+{c}\cos\varphi$',)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.axis('equal')

# 3) Koule kartezsky
xk_s = np.linspace(x0 - r, x0 + r, 100)
yk_s = np.linspace(y0 - r, y0 + r, 100)
Xkar_s, Ykar_s = np.meshgrid(xk_s, yk_s)

kk = r**2 - ((Xkar_s - x0)**2) - ((Ykar_s - y0)**2)
kk[kk < 0] = np.nan

kk1 = z0 + np.sqrt(kk)
kk2 = z0 - np.sqrt(kk)

ax3.plot_surface(Xkar_s, Ykar_s, kk1, cmap='Oranges', edgecolor='none', alpha=0.8)
ax3.plot_surface(Xkar_s, Ykar_s, kk2, cmap='Oranges', edgecolor='none', alpha=0.8)
ax3.set_title(rf'Koule (kartézsky): $(x-{x0})^2 + (y-{y0})^2 + (z-{z0})^2 = {r}^2$')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')
ax3.axis('equal')

# 4) Koule polarne
xsp = x0 + r * np.sin(P) * np.cos(U)
ysp = y0 + r * np.sin(P) * np.sin(U)
zsp = z0 + r * np.cos(P)

ax4.plot_surface(xsp, ysp, zsp, cmap='Purples', edgecolor='none', alpha=0.8)
ax4.set_title(rf'Koule (polárně): $x={x0}+{r}\sin\varphi\cos\theta,\ y={y0}+{r}\sin\varphi\sin\theta,\ z={z0}+{r}\cos\varphi$',)
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_zlabel('z')
ax4.axis('equal')


plt.suptitle('3D kuželosečka/kvadrika - Elipsoid a koule (polárně i kartézsky)', fontsize=14)
plt.tight_layout()
plt.show()