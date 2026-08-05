# Nakresli elipsu pres stredovou rovnici i pres polarizaci souradnic

import numpy as np
import matplotlib.pyplot as plt

# stred a poloosy
x0 = 2
y0 = 3
a = 3
b = 4

# 1) pres kartezsky system
x = np.linspace(x0-a-1, x0+a+1, 500)
y = np.linspace(y0-b-1, y0+b+1, 500)
X,Y = np.meshgrid(x, y)

# definujeme kartezskou funkci
F = ((X-x0)**2) /(a**2) + ((Y-y0)**2)/(b**2) - 1

# Numericke vykresleni
plt.contour(X, Y, F, levels=[0], colors='blue', linewidths=2)
plt.scatter(x0, y0, color='black', s=50)

plt.xlabel('x')
plt.ylabel('y')
plt.title(rf'Kartézsky: $\frac{{(x-{x0})^2}}{{{a}^2}} + \frac{{(y-{y0})^2}}{{{b}^2}} = 1$')
plt.grid(True, linestyle=':', alpha=0.6)

plt.show()

# -----------------------------------------------------------------

# 2) pres polarni system

uhel = np.linspace(0, 2*np.pi, 1000) # uhel mezi 0 a 2 pi (rad)

# soustava
ox = x0 + a*np.cos(uhel)
oy = y0 + b*np.sin(uhel)

# Vykresleni
plt.plot(ox, oy, color='crimson', linewidth=2)
plt.scatter(x0, y0, color='black', s=50)

plt.xlabel('x')
plt.ylabel('y')
plt.title(rf'Parametricky: $x = {x0} + {a}\cos(\varphi)$, $y = {y0} + {b}\sin(\varphi)$')
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()

