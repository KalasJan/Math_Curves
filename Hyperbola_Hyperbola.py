# Nakresli hyperbolu pres stredovou rovnici i pres polarizaci souradnic

import numpy as np
import matplotlib.pyplot as plt

# stred a poloosy
x0 = 2
y0 = 3
a = 3
b = 4

# 1) pres kartezsky system
x = np.linspace(x0-a-10, x0+a+10, 500)
y = np.linspace(y0-b-10, y0+b+10, 500)
X,Y = np.meshgrid(x, y)

# definujeme kartezskou funkci
F = ((X-x0)**2) /(a**2) - ((Y-y0)**2)/(b**2) - 1

# Numericke vykresleni
plt.contour(X, Y, F, levels=[0], colors='blue', linewidths=2)
plt.scatter(x0, y0, color='black', s=50)

# asymptoty
as1 = y0 + (b / a) * (x - x0)
as2 = y0 - (b / a) * (x - x0)

plt.plot(x, as1, color='gray', linestyle='--', linewidth=1.2, label='Asymptoty')
plt.plot(x, as2, color='gray', linestyle='--')

plt.xlabel('x')
plt.ylabel('y')
plt.title(rf'Kartézsky: $\frac{{(x-{x0})^2}}{{{a}^2}} - \frac{{(y-{y0})^2}}{{{b}^2}} = 1$')
plt.axis('equal') # Zajišťuje správný sklon asymptot (poměr stran b/a) na monitoru
plt.grid(True, linestyle=':', alpha=0.6)

plt.show()

# -----------------------------------------------------------------

# 2) pres polarni system

p = np.linspace(-2, 2, 500) #parametr

# soustava
vetev_x_pravo = x0 + a*np.cosh(p)
vetev_y_pravo = y0 + b*np.sinh(p) #nejjednodussi predpis pres hyperbolicky cosinus a sinus

vetev_x_levo = x0 - a*np.cosh(p)
vetev_y_levo = y0 + b*np.sinh(p)

# kresleni asymptot
x_asymptot = np.linspace(x0 - 15, x0 + 15, 500)
asy_1 = y0 + (b / a) * (x_asymptot - x0)
asy_2 = y0 - (b / a) * (x_asymptot - x0)

plt.plot(x_asymptot, asy_1, color='gray', linestyle='--', linewidth=1.2, label='Asymptoty')
plt.plot(x_asymptot, asy_2, color='gray', linestyle='--')


# Vykresleni hyperboly 
plt.plot(vetev_x_pravo, vetev_y_pravo, color='crimson', linewidth=2, label='Hyperbola')
plt.plot(vetev_x_levo, vetev_y_levo, color='crimson', linewidth=2)
plt.scatter(x0, y0, color='black', s=50)

plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Parametricky: $x = x_0 \pm a\cosh(t)$, $y = y_0 + b\sinh(t)$')
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()

