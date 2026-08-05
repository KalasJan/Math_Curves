# Vykresli graf tzv. Retezovky
# mame dano lano, uchopene na obou koncich. tvar proveseni je Retezovka

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve # pokud mame delku krivky

# 1) podle koeficientu a (parametr zakriveni)

a1 = 0.1 # parametr zakriveni

x = np.linspace(-3*a1, 3*a1, 500)

# definujeme kartezskou funkci
f = a1 * np.cosh(x/a1)

# Numericke vykresleni
plt.figure(figsize=(8, 6))
plt.plot(x, f, color='blue', linewidth=2)


plt.xlabel('x')
plt.ylabel('y')
plt.title(rf'Řetězovka $y = {a1} \cdot \cosh\left(\frac{{x}}{{{a1}}}\right)$')
plt.axis('equal') # jednotna delka os
plt.grid(True, linestyle=':', alpha=0.6)

plt.show()

# -------------------------------------------------------------------------------

# 2) je dana delka retezu

# L = 2*a2 * sinh (x0 / a2) - delka oblouhu na [-x0, x0]

L = 53 # jak dlouha ma byt krivka
x0 = 10 # ukotveni lana v (-x0, y0) a (x0,y0)

# definujeme funkci jako rovnici
def long(a2):
    return 2 * a2 * np.sinh(x0/a2) - L

# numericke reseni
a_sol = fsolve(long, 1)[0]

# graf pro delku
x = np.linspace(-x0, x0, 1000)
y = a_sol * np.cosh(x/a_sol)

plt.figure(figsize=(8, 5))
plt.plot(x, y, color='red', linewidth=2)
plt.scatter([-x0, x0], [y[0], y[-1]], color='black') # Body ukotvení
plt.title(f'Řetězovka o dané délce L={L}, a = {a_sol:.2f}')
plt.axis('equal') # jednotna delka os
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()



