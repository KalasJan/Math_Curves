# Nakresli Cassiniovy krivky / rezy torusu


import numpy as np
import matplotlib.pyplot as plt

# stred
x0, y0 = 0,0
a = 2 # vzdalenost stredu od ohniska

# kartezsky system
x = np.linspace(-4, 4, 600)
y = np.linspace(-3, 3, 600)
X, Y = np.meshgrid(x, y)

# rovnice
Xs = X - x0
Ys = Y - y0
L = (Xs**2 + Ys**2)**2 - 2 * (a**2) * (Xs**2 - Ys**2)
# P = c**4 - a**4

plt.figure(figsize=(10, 8))

# Typ 1: c < a -> 2 separovane utvary
c1 = 1.5
graf_1 = c1**4 - a**4

plt.contour(X, Y, L, levels=[graf_1], colors='blue', linewidths=3.5, linestyles='solid')
plt.plot([], [], color='blue', linewidth=3.5, label=rf'$c = {c1} < a = {a}$')
#linestyle -> graf_1 < 0 -> carkovany, linestyle ji vyplni na plnou cat

# Typ 2: c = a -> Lemniskáta (tvar nekonecna)
c2 = a
graf_2 = c2**4 - a**4

plt.contour(X, Y, L, levels=[graf_2], colors='crimson', linewidths=3.5)
plt.plot([], [], color='crimson', linewidth=3.5, label=rf'$c = {c2} = a = {a}$')

# Typ 3: c > a -> Oval
c3 = 3
graf_3 = c3**4 - a**4

plt.contour(X, Y, L, levels=[graf_3], colors='green', linewidths=3.5)
plt.plot([], [], color='green', linewidth=3.5, label=rf'$c= {c3} > a = {a}$')

# vyznamne body
plt.scatter([-a, a], [0, 0], color='darkorange', s=80, zorder=5, label='Ohniska')
plt.scatter(x0, y0, color='black', s=50, zorder=5, label = 'Střed')

# vse v jednom
plt.xlabel('x')
plt.ylabel('y')
plt.title('Rodina Cassiniových křivek', fontsize=14, fontweight='bold', pad=15)

plt.axis('equal') 
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend(loc='upper right', fontsize=12)

plt.show()


















