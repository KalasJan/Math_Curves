# Nakresli parabolu přes vrcholovou rovnici i přes parametrické souřadnice


import numpy as np
import matplotlib.pyplot as plt

# Vrchol a parametr p (vzdálenost ohniska od řídicí přímky)
x0 = 2
y0 = 3
p = 3 

# 1) PŘÍSTUP: Kartézský systém (Vrcholová implicitní rovnice)

# Vytvoření mříže bodů orientované ve směru otevírání paraboly (doprava)
x = np.linspace(x0 - 1, x0 + 10, 500)
y = np.linspace(y0 - 6, y0 + 6, 500)
X, Y = np.meshgrid(x, y)

# Definujeme kartézskou implicitní funkci F(X, Y) = 0
F = (Y - y0)**2 - 2 * p * (X - x0)


# Vykreslení nulové vrstevnice (samotná křivka paraboly)
plt.contour(X, Y, F, levels=[0], colors='blue', linewidths=2)
plt.scatter(x0, y0, color='black', s=50)

plt.xlabel('x')
plt.ylabel('y')
plt.title(rf'Kartézsky: $(y-{y0})^2 = 2 \cdot {p} \cdot (x-{x0})$', fontsize=12)

# Oříznutí pohledu, aby graf přesně kopíroval vypočtená data a nebyl deformovaný
plt.axis('equal') 
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()

# -----------------------------------------------------------------
# 2) PŘÍSTUP: Parametrický systém (Parametr t)


t = np.linspace(-3, 3, 400) # Parametr t pro parametrické vyjádření (reprezentuje rozsah tečen)

# Soustava parametrických rovnic
ox = x0 + (p * t**2) / 2
oy = y0 + p * t 

plt.plot(ox, oy, color='darkcyan', linewidth=2)
plt.scatter(x0, y0, color='black', s=50)

plt.xlabel('x')
plt.ylabel('y')
plt.title(rf'Parametricky: $x = {x0} + \frac{{{p} \cdot t^2}}{{2}}$, $y = {y0} + {p} \cdot t$', fontsize=12)
plt.axis('equal') 
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()
