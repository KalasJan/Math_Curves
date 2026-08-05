# Nakresli Kardioidu
# jde pouze parametricky

import numpy as np
import matplotlib.pyplot as plt

# parametry
a = 0.5 # polomer kruznice
x0, y0 = 3, 4 # pocatek

uhel = np.linspace(0, 2*np.pi, 1000) # uhel otoceni 

# soustava
ox = x0 + 2*a*(1-np.cos(uhel)) * np.cos(uhel)
oy = y0 + 2*a*(1-np.cos(uhel))*np.sin(uhel)

# Vykresleni Kardioidy
 
plt.plot(ox, oy, color='darkcyan', linewidth=2)
plt.scatter(x0, y0, color='black', s=50)

plt.xlabel('x')
plt.ylabel('y')
plt.title(rf'Kardioida: $x = {x0} + 2 \cdot {a} \cdot (1-\cos(\varphi)) \cdot \cos(\varphi)$, $y = {y0} + 2 \cdot {a} \cdot (1-\cos(\varphi)) \cdot \sin(\varphi)$', fontsize=12)
plt.axis('equal') # jinak se srdce protahne
plt.tight_layout()
plt.show()

