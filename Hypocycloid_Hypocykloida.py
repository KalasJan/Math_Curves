# Nakresli Hypocykloidu
# pozn.: k = 4 ... astroida

import numpy as np
import matplotlib.pyplot as plt

# parametry
k = 4 # pocet vrcholu, pomer R/r (R - velka "kruznice")
r = 2 # polomer male kruznice
x0, y0 = 3, 4 # pocatek
R = k * r

uhel = np.linspace(0, 2*np.pi, 1000) # uhel otoceni 

# soustava
ox = x0 + r*(k-1)*np.cos(uhel) + r*np.cos((k-1)*uhel)
oy = y0 + r*(k-1)*np.sin(uhel) - r*np.sin((k-1)*uhel)

# Vodicí pevná kružnice (šedá, čárkovaná), uvnitř které se malá valí
uhel_kruznice = np.linspace(0, 2*np.pi, 500)
kx = x0 + R * np.cos(uhel_kruznice)
ky = y0 + R * np.sin(uhel_kruznice)
plt.plot(kx, ky, color='gray', linestyle='--', linewidth=1.5, alpha=0.7, label=f'Pevná kružnice ($R={R}$)')


# Vykresleni Hypocykloidy
 
plt.plot(ox, oy, color='navy', linewidth=2)
plt.scatter(x0, y0, color='black', s=50)

plt.xlabel('x')
plt.ylabel('y')
plt.title(rf'Hypocykloida: $r = {r}, k = {k}$', fontsize=12)
plt.axis('equal') # jinak vrcholy nebudou na kruznici, ale vizualne na elipse
plt.tight_layout()
plt.show()

