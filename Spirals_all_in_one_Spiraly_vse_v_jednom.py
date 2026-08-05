# Nakresli všechny Spirály v polárních  souřadnicích
# Archimedova, Hyperbolicka, Logaritmicka, Fermatova, Lituus

import numpy as np
import matplotlib.pyplot as plt

# Parametry
a = 0.5
b = 0.1
uhel = np.linspace(0.1, 10*np.pi, 1000) 
# 0.1 kvuli deleni nulou u nekterych spiral

# Definice spirál
spiraly = [
    (a * uhel, 'Archimédova', r'$r = a \cdot \varphi$'),
    (a / uhel, 'Hyperbolická', r'$r = a / \varphi$'),
    (a * np.exp(b * uhel), 'Logaritmická', r'$r = a \cdot e^{b\varphi}$'),
    (a * np.sqrt(uhel), 'Fermatova', r'$r = a \cdot \sqrt{\varphi}$'),
    (a / np.sqrt(uhel), 'Lituus', r'$r = a / \sqrt{\varphi}$')
]

# Vytvoření figury se subploty
fig = plt.figure(figsize=(15, 10))
plt.suptitle(f'Přehled spirál (a={a}, b={b})', fontsize=16, fontweight='bold')

for i, (r, nazev, rovnice) in enumerate(spiraly, 1):
    ax = fig.add_subplot(2, 3, i, projection='polar')
    ax.plot(uhel, r, color='darkcyan', linewidth=1.5)
    ax.set_title(f'{nazev}\n{rovnice}', fontsize=10)
    ax.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()