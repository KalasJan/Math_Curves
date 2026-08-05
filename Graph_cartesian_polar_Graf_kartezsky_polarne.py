# Nakresli grafy funkci y = sin(a*x)+cos (b*x) kartezsky i polarne

import numpy as np
import matplotlib.pyplot as plt

#parametry
a = 3
b = 5

# popisy os
ox = np.linspace(0, 4*np.pi, 1000) # v polarnich ma funkci uhlu
oy = np.sin(a*ox) + np.cos (b*ox)

# 2 grafy vedle seme (L - kartezsky, P - polarne)
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8)) - moznost 1
fig = plt.figure(figsize=(16, 8))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122, projection='polar') # polarni system

# Kartezsky
ax1.plot(ox, oy, linewidth=2)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title('Graf v karteziánských souřadnicích')
ax1.grid(True)

# Polarne
# ax2.remove() #smazeme kartezsky system

ax2.plot(ox, oy, color='Green', linewidth=2)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.set_title('Graf v polárních souřadnicích',fontsize=12)

# titulek
plt.suptitle(rf'Graf funkce $y = \sin({a}x)+\cos({b}x)$', fontsize=14)
plt.tight_layout()
plt.show()