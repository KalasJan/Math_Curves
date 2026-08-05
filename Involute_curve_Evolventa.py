# Vykresleni tvz. Evolventy / Involute curve

import numpy as np
import matplotlib.pyplot as plt

# parametry
par = np.linspace(0, 4 *np.pi, 1000)
pol = 1 # polomer zakladni kruznice (od ktere se odviji)

# analytika
ox = pol * (np.cos(par) + par * np.sin(par))
oy = pol * (np.sin(par) - par * np.cos(par))

# polarni
r_inv = np.sqrt(ox**2 + oy**2)
uhel_inv = np.arctan2(oy, ox)

# kresleni

# knuznice od niz se odmotava
uhel_kruz = np.linspace(0, 2 * np.pi, 200) 
plt.plot(pol * np.cos(uhel_kruz), pol * np.sin(uhel_kruz), color = 'green',linestyle ='-.', alpha=1, label='Základní kružnice')

plt.plot(ox, oy, color='crimson', linewidth=2, label='Evolventa')

plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis('equal')
plt.title(rf"Evolventa kružnice se základním poloměrem $a = {pol}$", fontsize=12)
plt.legend()

plt.show()