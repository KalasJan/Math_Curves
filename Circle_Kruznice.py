# Nakresli kruznici pres stredovou rovnici i pres polarizaci souradnic

import numpy as np
import matplotlib.pyplot as plt

# stred a polomer
x0 = 2
y0 = 3
r = 1

# 1) pres kartezsky system
x = np.linspace(x0-r-1, x0+r+1, 500)
y = np.linspace(y0-r-1, y0+r+1, 500)
X,Y = np.meshgrid(x, y)

# definujeme kartezskou funkci
F = (X-x0)**2 + (Y-y0)**2 - r**2

# Numericke vykresleni
plt.contour(X, Y, F, levels=[0], colors='blue', linewidths=2)
plt.scatter(x0, y0, color='black', s=50)

plt.xlabel('x')
plt.ylabel('y')
plt.title(rf'Kartézsky: $(x-{x0})^2 + (y-{y0})^2 = {r}^2$')
plt.axis('equal')  # Velmi důležité! Bez tohoto by kružnice vypadala jako elipsa
plt.grid(True, linestyle=':', alpha=0.6)

plt.show()

# -----------------------------------------------------------------

# 2) pres polarni system

uhel = np.linspace(0, 2*np.pi, 1000) # uhel mezi 0 a 2 pi (rad)

# soustava
ox = x0 + r*np.cos(uhel)
oy = y0 + r*np.sin(uhel)

# Vykresleni
plt.plot(ox, oy, color='crimson', linewidth=2)
plt.scatter(x0, y0, color='black', s=50)

plt.xlabel('x')
plt.ylabel('y')
plt.title(rf'Parametricky: $x = {x0} + {r}\cos(\varphi)$, $y = {y0} + {r}\sin(\varphi)$')
plt.axis('equal')  # Zajišťuje dokonalý kruh
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()

