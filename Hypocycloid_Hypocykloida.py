# Nakresli Hypocykloidu
# pozn.: k = 4 ... astroida

import numpy as np
import matplotlib.pyplot as plt

# parametry
k = 3 # pocet vrcholu, pomer R/r (R - velka "kruznice")
r = 2 # polomer male kruznice
x0, y0 = 3, 4 # pocatek

uhel = np.linspace(0, 2*np.pi, 1000) # uhel otoceni 

# soustava
ox = x0 + r*(k-1)*np.cos(uhel) + r*np.cos((k-1)*uhel)
oy = y0 + r*(k-1)*np.sin(uhel) - r*np.sin((k-1)*uhel)

# Vykresleni Hypocykloidy
 
plt.plot(ox, oy, color='navy', linewidth=2)
plt.scatter(x0, y0, color='black', s=50)

plt.xlabel('x')
plt.ylabel('y')
plt.title(rf'Hypocykloida: $r = {r}, k = {k}$', fontsize=12)
plt.axis('equal') # jinak vrcholy nebudou na kruznici, ale vizualne na elipse
plt.tight_layout()
plt.show()

