#○ Vykresli 3d krivku - Sroubovici

import numpy as np
import matplotlib.pyplot as plt3d

# 1) Parametry šroubovice
R = 40      # Poloměr válce, na ktery se drat mota
c = 4     # Koeficient stoupání (jak rychle roste do výšky)

# Rozsah úhlu (uděláme 4 plné otočky: 4 * 2pi = 8pi)
uhel = np.linspace(0, 8 * np.pi, 1000)

# Rovnice šroubovice
x = R * np.cos(uhel)
y = R * np.sin(uhel)
z = c * uhel

# 2) Vytvoření plátna pro dva grafy
fig = plt3d.figure(figsize=(16, 8))

# 3D graf šroubovice
ax = fig.add_subplot(111, projection='3d')

ax.view_init(elev=45, azim=45) #otoceni

ax.plot(x, y, z, color='blue', linewidth=3, label='Šroubovice (Helix)')
ax.set_xlabel('Osa X')
ax.set_ylabel('Osa Y')
ax.set_zlabel('Osa Z (Výška)')
ax.set_title(rf'Šroubovice ve 3D prostoru kolem válce o poloměru {R} a rychlosti stoupani {c}')
plt3d.grid(True)

plt3d.show()