# Nakresli Elipticky, Rotacni a Hyperbolicky Paraboloid

import numpy as np
import matplotlib.pyplot as plt

# stred a poloosy
x0 = 2
y0 = 3
z0 = 1
a = 2
b = 7
c = 2

x = np.linspace(x0-a-1, x0+a+1, 500)
y = np.linspace(y0-b-1, y0+b+1, 500)
X,Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(18, 6))
ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')

# 1) Elipticky
Ze = c * (((X-x0)**2) /(a**2) + ((Y-y0)**2)/(b**2)) + z0

# kresleni
ax1.plot_surface(X, Y, Ze, cmap='Blues', edgecolor='none', alpha=0.8)
ax1.set_title(rf'Eliptický paraboloid, $\frac{{(x-{x0})^2}}{{{a}^2}} + \frac{{(y-{y0})^2}}{{{b}^2}} = {2*c}(z -{z0}) $')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.axis('equal')

# 2) Rotacni
Zr = c * (((X-x0)**2) /(a**2) + ((Y-y0)**2)/(a**2)) + z0

ax2.plot_surface(X, Y, Zr, cmap='Greens', edgecolor='none', alpha=0.8)
ax2.set_title(rf'Rotační paraboloid, $\frac{{(x-{x0})^2}}{{{a}^2}} + \frac{{(y-{y0})^2}}{{{a}^2}} = {2*c}(z -{z0}) $')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.axis('equal')

# 3) Hyperbolicky
Zh = c * (((X-x0)**2) /(a**2) - ((Y-y0)**2)/(b**2)) + z0

ax3.plot_surface(X, Y, Zh, cmap='Oranges', edgecolor='none', alpha=0.8)
ax3.set_title(rf'Hyperbolický paraboloid, $\frac{{(x-{x0})^2}}{{{a}^2}} - \frac{{(y-{y0})^2}}{{{a}^2}} = {2*c}(z -{z0}) $')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')
ax3.axis('equal')


plt.suptitle('3D kuželosečka/kvadrika - Paraboloid', fontsize=14)
plt.tight_layout()
plt.show()