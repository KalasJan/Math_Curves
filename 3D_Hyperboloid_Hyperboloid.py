# Nakresli Jednodilny (i specialni Jested) i Dvojdilny Hyperboloid

import numpy as np
import matplotlib.pyplot as plt

# stred a poloosy
x0 = 2
y0 = 3
z0 = 1 # posun ve smyslu středu/výšky
ruz = 1 # polomer v nejuzsim miste
a = 2
b = 7
c = 2

x = np.linspace(0, 2 * np.pi, 500) # 
y1 = np.linspace(-2, 2, 100)    # parametr pro jednodílný hyperboloid
y2 = np.linspace(0, 2, 100)    # parametr pro dvoudílný hyperboloid
yj = np.linspace(-4, 0, 100) # pro Jested

X,Y1 = np.meshgrid(x, y1)
_, Y2 = np.meshgrid(x, y2)
_, Yj = np.meshgrid(x, yj)

fig = plt.figure(figsize=(18, 6))
ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')

# 1) "Jested"
xl = x0 + ruz * np.cosh(Yj) * np.cos(X)
yl = y0 + ruz * np.cosh(Yj) * np.sin(X)
zl = z0 + c * np.sinh(Yj)

ax1.plot_surface(xl, yl, zl, cmap='rainbow', edgecolor='none', alpha=0.9,)
ax1.set_title(rf'Ještěd (rotační jednodílný hyperboloid): $\frac{{(x-{x0})^2}}{{{ruz}^2}} + \frac{{(y-{y0})^2}}{{{ruz}^2}} - \frac{{(z-{z0})^2}}{{{c}^2}} = 1$',
    fontsize=10,
)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.axis('equal')

# 2) Jednodilny
xj = x0 + a * np.cosh(Y1) * np.cos(X)
yj = y0 + b * np.cosh(Y1) * np.sin(X)
zj = z0 + c * np.sinh(Y1)

# kresleni
ax2.plot_surface(xj, yj, zj, cmap='copper', edgecolor='none', alpha=0.8)
ax2.set_title(rf'Jednodílný hyperboloid: $\frac{{(x-{x0})^2}}{{{a}^2}} + \frac{{(y-{y0})^2}}{{{b}^2}} - \frac{{(z-{z0})^2}}{{{c}^2}} = 1$')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.axis('equal')


# 3) Dvoudilny
xd = x0 + a * np.sinh(Y2) * np.cos(X)
yd = y0 + b * np.sinh(Y2) * np.sin(X)
zd_horni = z0 + c * np.cosh(Y2)
zd_dolni = z0 - c * np.cosh(Y2)

ax3.plot_surface(xd, yd, zd_horni, cmap='seismic', edgecolor='none', alpha=0.8)
ax3.plot_surface(xd, yd, zd_dolni, cmap='seismic', edgecolor='none', alpha=0.8)
ax3.set_title(rf'Dvoudílný hyperboloid, $\frac{{(x-{x0})^2}}{{{a}^2}} + \frac{{(y-{y0})^2}}{{{b}^2}} - \frac{{(z-{z0})^2}}{{{c}^2}} = -1$')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')
ax3.axis('equal')


plt.suptitle('3D kuželosečka/kvadrika - Hyperboloid', fontsize=14)
plt.tight_layout()
plt.show()